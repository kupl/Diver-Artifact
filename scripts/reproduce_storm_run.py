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
MODE = ""
TIEMOUT = 0
KILL_TIMEOUT = 0
OUTPUT_DIR = ""
CORE = 0
BENCHMARK = ""
INIT_VALUE = 0

def setup_globals(args,output):
    global MODE
    global TIMEOUT
    global KILL_TIMEOUT
    global CORE
    global OUTPUT_DIR

    MODE = "/reproduce_storm"
    TIMEOUT = args.time
    KILL_TIMEOUT = TIMEOUT+10
    CORE = args.core
    OUTPUT_DIR = output


def get_cmd(diver_path,idx):
    cmd = []
    if idx == 1:
        cmd = ['docker', 'run', '--rm', '-v',diver_path+':/Diver/bug_dir','jongwook123/diver:icse2023-artifact','timeout',str(KILL_TIMEOUT),'python3','__main__.py',
        '--solver','z3', '--solverapi','z3','--solverbin','/solvers/z3-a069b65/build/z3','--benchmark','Section_IV/Regenerate/'+BENCHMARK,'--logic','QF_SLIA']
    elif idx == 2:
        cmd = ['docker', 'run', '--rm', '-v',diver_path+':/Diver/bug_dir','jongwook123/diver:icse2023-artifact','timeout',str(KILL_TIMEOUT),'python3','__main__.py',
        '--solver','z3', '--solverapi','z3','--solverbin','/solvers/z3-0146259/build/z3','--benchmark','Section_IV/Regenerate/'+BENCHMARK,'--logic','QF_SLIA','--option','smt.string_solver=z3str3']
    return cmd


def run(task):
    bench = BENCHMARK.split('.')[0]
    idx = int(bench.split('_')[-1])
    LOCK.acquire()
    cnt.value += 1
    print(BENCHMARK+' processing '+str(cnt.value)+'/'+str(CORE+INIT_VALUE))
    diver_path = OUTPUT_DIR+MODE+"/run_"+str(cnt.value)+"/"+bench
    if not os.path.exists(diver_path):
        os.makedirs(diver_path)
    cmd = get_cmd(diver_path,idx)
    print(' '.join(cmd))
    LOCK.release()

    run_time = datetime.now()
    start = time.time()
    p = subprocess.Popen(cmd, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr=subprocess.STDOUT)
    log = p.stdout.read()
    end = time.time()

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
    parser.add_argument('--time', type=int, help = 'timeout(s) for each benchmark', default=3600)
    parser.add_argument('--core', type=int, help = 'number of cores for parellel running',default=30)

    args = parser.parse_args()

    if not os.path.exists(default_output):
        os.mkdir(default_output)

    print(f'Output Directory made: {default_output}')
    setup_globals(args,default_output)
    num_task = args.core
    tasks = [i+1 for i in range(num_task)]

    LOCK.acquire()
    cnt.value = 0
    LOCK.release()

    diver_path = OUTPUT_DIR+MODE

    if os.path.exists(diver_path):
        dirs = os.listdir(diver_path)
        cur_jobs = []
        for dir in dirs:
            cur_jobs.append(int(dir.split('_')[-1]))
        cur_jobs.sort()
        LOCK.acquire()
        cnt.value = cur_jobs[-1]
        INIT_VALUE = cur_jobs[-1]
        LOCK.release()


    for i in range(1,3):
        BENCHMARK = "storm_bench_"+str(i)+".smt2"
        pool = Pool(args.core)
        pool.map(run,tasks)
        pool.close()
        pool.join()

if __name__ == "__main__":
    main()