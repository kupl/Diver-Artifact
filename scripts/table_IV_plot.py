import argparse
import os, sys
import subprocess
import shutil
import random
from z3 import *

def get_yinyang_logs(path_to_dir):
    file_paths = list()
    for r, d, f in os.walk(path_to_dir):
        for file in f:
            if ".output" in file:
                file_paths.append(os.path.join(r,file))
    return file_paths

def get_logs(path_to_dir):
    file_paths = list()
    for r, d, f in os.walk(path_to_dir):
        for file in f:
            if ".log" in file:
                file_paths.append(os.path.join(r,file))
    return file_paths

def get_bugs(path_to_dir):
    file_paths = list()
    for r, d, f in os.walk(path_to_dir):
        for file in f:
            if ".smt2" in file:
                file_paths.append(os.path.join(r,file))
    return file_paths 

def print_bug_status(status):
    print("|---------------------------------------|")
    print("|  Benchmark_ID   |  Bug Finding Result |")
    print("|---------------------------------------|")
    find_res = 0
    fail_res = 0
    for idx in range(1,26):
        print("| {0:^15} | {1:^20}|".format("bench_"+str(idx)+".smt2",status[idx]))
        if status[idx]=="O":
            find_res += 1
        else:
            fail_res += 1
    print("|---------------------------------------|")
    print("| #Total: {0:^2} | #Success: {1:^2} | #Fail: {2:^2} |".format(25,str(find_res),str(fail_res)))
    return

def get_idx(log):
    idx = 0
    d = log.split('/')
    for c in d:
        k = c.split('_')
        if k[0]=="bench":
            idx =int(k[1])
            break
    return idx


def judge(file,idx):
    set_param("model",True)
    set_option("model_validate","true")
    s = Solver()
    s.set("timeout", 10000)
    ast = parse_smt2_file(file)
    s.add(ast[0])
    if s.check() == sat:
        model = s.model()
        if (len(model) <= 2 and idx == 11) or (len(model)<=1 and idx ==12):
            return False
        for m in model:
            md = str(m)
            if md == "/0": 
                return False
    else:
        return False
    return True

def get_yinyang_bugs(path, bug_type):
    logs = get_yinyang_logs(path)
    bugs = get_bugs(path)
    # ./output/tool/run_x/bench/bug/y.output
    # ./output/tool/run_x/bench/log/x.log
    status = ["X" for i in range(26)]
    checked_ = ["X" for i in range(26)]
    for log in logs:
        idx = get_idx(log)

        if "crash" in log and bug_type[idx]:
            f = open(log,'r')
            datas = f.readlines()
            f.close()
            for data in datas:
                if ("an invalid model was generated" in data or "ERRORS SATISFYING ASSERTIONS WITH MODEL:") and bug_type[idx]=="invalid":
                    status[idx]="O"
                    break
                elif bug_type[idx]=="crash":
                    status[idx]="O"
                    break
        elif "incorrect" in log and bug_type[idx]=="soundness":
            f = open(log,'r')
            datas = f.readlines()
            f.close()
            p = False
            file_path = ""
            for data in datas:
                if "sat" in data:
                    p = True
                    if idx not in [11,12]:
                        status[idx]="O"
                    break
            if p and idx in [11,12] and checked_[idx]=="X":
                for b in bugs:
                    c = b.split('/')[-3].split('_')[-1]
                    if int(c) == idx:
                        res = judge(b,idx)
                        if res:
                            status[idx]="O"
                            break
                checked_[idx] = "O"
                
    return status


def get_storm_bugs(path,bug_type):
    logs = get_logs(path)
    status = ["X" for i in range(26)]
    for log in logs:
        idx = int(log.split('/')[-2].split('_')[1])
        f = open(log,'r')
        datas = f.readlines()
        f.close()
        for data in datas:
            k = data.split()
            if "assertviolation" in data and bug_type[idx]=="invalid":
                status[idx] = "O"
            elif "unsat" in data and bug_type[idx] == "soundness":
                status[idx] = "O"
            elif "fatalfailure" in data and bug_type[idx] == "crash":
                status[idx] = "O"

    return status


def get_autostring_bugs(path, bug_type):
    logs = get_logs(path)
    # ./output/autostring/run_x/bench_x/y.log
    status = ["X" for i in range(26)]
    for log in logs:
        idx = int(log.split('/')[-2].split('_')[1])
        f = open(log,'r')
        datas = f.readlines()
        f.close()
        for data in datas:
            if data == "unsat" and bug_type[idx] == "soundness":
                status[idx] = "O"
                break
            elif data == "invalid" and bug_type[idx] == "invalid":
                status[idx] = "O"
                break
            elif data == "crash" and bug_type[idx] == "crash":
                status[idx] = "O"
                break
    return status


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, help = "path of directory")
    args = parser.parse_args()
    
    bug_type = ["soundness" for i in range(0,13)]+["invalid" for i in range(9)]+["crash" for i in range(4)]

    tool = args.input.split('/')[-1]

    status = ["X" for i in range(26)]
    if tool in ["typefuzz","opfuzz","fusion"]:
        status = get_yinyang_bugs(args.input,bug_type)
    elif tool == "autostring":
        status = get_autostring_bugs(args.input,bug_type)
    elif tool == "storm":
        status = get_storm_bugs(args.input,bug_type)
    else:
        return
    print_bug_status(status)
    return

if __name__=='__main__':
    main()