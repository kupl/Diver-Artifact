import sys
import os
import time
import csv
import json
import subprocess
import multiprocessing
import shutil
import argparse
from datetime import datetime
from multiprocessing import Pool, Lock, Value
from os.path import expanduser


LOCK = multiprocessing.Lock()
cnt = Value ('i',0)
TOOL = ""
TIEMOUT = 0
KILL_TIMEOUT = 0
S_TIMEOUT = 0
OUTPUT_DIR = ""
CORE = 0
MUTANTS = 0
BENCHMARK = ""
INIT_VALUE = 0

def setup_globals(args,output):
    global TOOL
    global TIMEOUT
    global KILL_TIMEOUT
    global CORE
    global OUTPUT_DIR
    global S_TIMEOUT

    TOOL = args.tool
    TIMEOUT = args.time
    KILL_TIMEOUT = TIMEOUT+10
    CORE = args.core
    OUTPUT_DIR = output
    MUTANTS = args.mutants
    S_TIMEOUT = args.solver_time

def get_status():
    global INIT_VALUE
    path = {"typefuzz": '/typefuzz', "opfuzz": '/opfuzz', "storm": '/storm', "autostring": '/autostring', "fusion": '/fusion'}
    tool_path = OUTPUT_DIR+path[TOOL]

    if os.path.exists(tool_path):
        dirs = os.listdir(tool_path)
        cur_jobs = []
        for dir in dirs:
            cur_jobs.append(int(dir.split('_')[-1]))

        idx = 0

        for job in cur_jobs:
            cur_benches = os.listdir(tool_path+"/run_"+str(job))
            if len(cur_benches)==25 and idx<job:
                idx = job

        LOCK.acquire()
        cnt.value = idx
        INIT_VALUE = idx
        LOCK.release()
    return

def get_solvers(bench):
    if bench in [5,6,7,20]:
        solver = "Z3str3"
    else:
        solver = "CVC5"
    return solver

def get_cmd(path):
    if TOOL == "autostring":
        bench = int(BENCHMARK.split('.')[0].split('_')[-1])
        solver = get_solvers(bench)
        cmd = ['docker', 'run', '--rm','-v', path+':/output','jongwook123/diver-artifact-autostring-icse2023:icse', './test.sh',str(KILL_TIMEOUT),solver,str(bench)]
    else:
        cmd = ['docker', 'run', '--rm', '-v',path+':/Diver/output','jongwook123/diver:icse2023-artifact','timeout',str(KILL_TIMEOUT),'python3','scripts/table_IV_run_tool.py','--tool',TOOL,'--time',str(TIMEOUT), '--benchmark', BENCHMARK, '--solver_time',str(S_TIMEOUT)]
    return cmd

def run(task):
    bench = BENCHMARK.split('.')[0]
    path = {"typefuzz": '/typefuzz', "opfuzz": '/opfuzz', "storm": '/storm', "autostring": '/autostring', "fusion": '/fusion'}
    LOCK.acquire()
    cnt.value += 1
    print('processing '+str(cnt.value)+'/'+str(CORE+INIT_VALUE))
    tool_path = OUTPUT_DIR+path[TOOL]+"/run_"+str(cnt.value)+"/"+bench
    if not os.path.exists(tool_path):
        os.makedirs(tool_path)
    cmd = get_cmd(tool_path)
    print(' '.join(cmd))
    LOCK.release()

    run_time = datetime.now()
    start = time.time()
    p = subprocess.Popen(cmd, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr=subprocess.STDOUT)
    log = p.stdout.read()
    end = time.time()
    slog = log.decode().split('\n')

    exec_time = end-start
    p.wait()
    p.poll()
    return 

def main():
    global BENCHMARK
    global INIT_VALUE
    # current directory path 
    path = os.path.dirname(os.path.abspath(__file__))
    current_dir = '/'.join(path.split('/')[:-1])
    default_output = os.path.join(current_dir,"output")

    parser = argparse.ArgumentParser()
    parser.add_argument('--tool', type=str, help = 'the tool for testing, tool = [typefuzz, opfuzz, storm, autostring, fusion]')
    parser.add_argument('--time', type=int, help = 'timeout(s) for each benchmark', default=3600)
    parser.add_argument('--core', type=int, help = 'number of cores for parellel running',default=30)
    parser.add_argument('--mutants', type=int, help = 'number of mutants generated by each tool per benchmark', default=2000000)
    parser.add_argument('--benchmark', type=str, help = 'benchmark for input = [ALL, bench_1.smt2, bench_2.smt2, ..., bench_25.smt2]', default="ALL")
    parser.add_argument('--solver_time', type=int, help = 'timeout(s) for SMT solver', default=10)
    args = parser.parse_args()

    if not os.path.exists(default_output):
        os.mkdir(default_output)

    print(f'Output Directory made: {default_output}')
    setup_globals(args,default_output)

    num_task = args.core
    tasks = [i+1 for i in range(num_task)]


    if args.benchmark == "ALL":
        for i in range(1,26):
            BENCHMARK = "bench_"+str(i)+".smt2"
            LOCK.acquire()
            cnt.value = 0
            LOCK.release()
            get_status()
            pool = Pool(args.core)
            pool.map(run,tasks)
            pool.close()
            pool.join()
    else:
        BENCHMARK = args.benchmark
        pool = Pool(args.core)
        pool.map(run,tasks)
        pool.close()
        pool.join()

if __name__ == "__main__":
    main()