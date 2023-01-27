import argparse
import os, sys
import subprocess
import shutil
import time
import logging
from datetime import datetime


NUM_BUGS = 0

def get_logs(path):
    logs = list()
    for r, d, f in os.walk(path):
        for file in f:
            if ".log" in file:
                logs.append(os.path.join(r,file))
    return logs


def get_bugs(path):
    bugs = list()
    for r, d, f in os.walk(path):
        for file in f:
            if ".smt2" in file:
                bugs.append(os.path.join(r,file))
    return bugs

def get_time(data):
    dates = data[0].split('-')
    year = int(dates[0][1:])
    month = int(dates[1])
    day = int(dates[2])
    time = data[1].split(':')
    hr = int(time[0])
    m = int(time[1])
    sec = int(time[2][:2])

    return datetime(year,month,day,hr,m,sec)

def make_statistics(logs):
    bug_type = ["Soundness" for i in range(0,13)]+["Model" for i in range(9)]+["Crash" for i in range(4)]
    cores = [[0 for i in range(31)] for i in range(26)]
    min_time = [ datetime(2032,1,1,0,0,0)-datetime.now() for i in range(26)]
    max_time = [ datetime.now()-datetime.now() for i in range(26) ]
    
    number_of_gen = [ 0 for i in range(26)]
    number_of_mutants = [ 0 for i in range(26)]
    sat_time = [0.0 for i in range(26)]
    unsat_time = [0.0 for i in range(26)]
    testing_time = [0.0 for i in range(26)]
    gen_time = [0.0 for i in range(26)]
    judge_time = [0.0 for i in range(26)]

    number_of_sat_mutants = [0 for i in range(26)]
    number_of_unsat_mutants = [0 for i in range(26)]


    number_of_gen_core = [ [0 for j in range(31)] for i in range(26)]
    number_of_mutants_core = [ [0 for j in range(31)] for i in range(26)]

    number_of_sat_mutants_core = [ [0 for j in range(31)] for i in range(26)]
    number_of_unsat_mutants_core = [ [0 for j in range(31)] for i in range(26)]


    sat_time_core = [ [0.0 for j in range(31)] for i in range(26)]
    unsat_time_core = [ [0.0 for j in range(31)] for i in range(26)]
    testing_time_core = [ [0.0 for j in range(31)] for i in range(26)]
    judge_time_core = [ [0.0 for j in range(31)] for i in range(26)]
    gen_time_core = [ [0.0 for j in range(31)] for i in range(26)]


    for log in logs:
        f = open(log,'r')
        datas = f.readlines()
        f.close()
        #./output/diver/run_x/bug_x/soundness/sx.smt2
        #print(log)
        bench = log.split('/')[-2]
        idx = int(bench.split('_')[1])
        core = int(log.split('/')[-3].split('_')[-1])
        start_time = get_time(datas[0].split())
        
        sat_mutants = 0
        unsat_mutants = 0

        for j in range(1,len(datas)):
            data = datas[j]
            d = data.split()
            if d[-1]=="Bug" and bug_type[idx] == d[-2]:
                buggy_time = get_time(d)
                cur_time = buggy_time-start_time
                min_time[idx] = min(min_time[idx],cur_time)
                max_time[idx] = max(max_time[idx],cur_time)
                if cores[idx][core] == 0:
                    cores[idx][core] = 1
            elif d[-1] != "Bug":
                if d[7] == "sat" or d[7] == "invalid":
                    sat_mutants+=1
                elif d[7] == "unsat":
                    unsat_mutants+=1
                else:
                    pass
            
        it = -1 
        while "Bug" in datas[it]:
            it -=1 
        last = datas[it]

        number_of_sat_mutants[idx] += sat_mutants
        number_of_sat_mutants_core[idx][core] = sat_mutants

        number_of_unsat_mutants[idx] += unsat_mutants
        number_of_unsat_mutants_core[idx][core] = unsat_mutants

        number_of_gen_core[idx][core] = int(float(last.split()[5]))
        number_of_gen[idx] += int(float(last.split()[5]))

        number_of_mutants_core[idx][core] = int(last.split()[3])
        number_of_mutants[idx] += int(last.split()[3])
    
        sat_time[idx] += float(last.split()[9])
        sat_time_core[idx][core] = float(last.split()[9])

        unsat_time[idx] += float(last.split()[11])
        unsat_time_core[idx][core] = float(last.split()[11])

        testing_time[idx] += float(last.split()[13])
        testing_time_core[idx][core] = float(last.split()[13])

        gen_time[idx] += float(last.split()[15])
        gen_time_core[idx][core] = float(last.split()[15])

        judge_time[idx] += float(last.split()[17])
        judge_time_core[idx][core] = float(last.split()[17])

    infos = [min_time,max_time,number_of_gen,number_of_mutants, cores, number_of_sat_mutants, number_of_unsat_mutants, sat_time, unsat_time, testing_time, gen_time, judge_time]
    core_infos = [number_of_gen_core,number_of_mutants_core, number_of_sat_mutants_core, number_of_unsat_mutants_core, sat_time_core, unsat_time_core, testing_time_core, gen_time_core, judge_time_core]

    return infos, core_infos



def make_statistics2(logs):
    cores = [[0 for i in range(31)] for i in range(26)]
    min_time = [ datetime(2032,1,1,0,0,0)-datetime.now() for i in range(26)]
    max_time = [ datetime.now()-datetime.now() for i in range(26) ]
    number_of_gen = [ 0 for i in range(26)]
    number_of_test = [ 0 for i in range(26)]
    for log in logs:
        f = open(log,'r')
        datas = f.readlines()
        f.close()
        #./output/diver/run_x/bug_x/soundness/sx.smt2
        #print(log)
        bench = log.split('/')[-2]
        idx = int(bench.split('_')[1])
        core = int(log.split('/')[-3].split('_')[-1])
        start_time = get_time(datas[0].split())
        for data in datas:
            d = data.split()
            if d[-1]=="Bug" and d[-2] == "Model":
                buggy_time = get_time(d)
                cur_time = buggy_time-start_time
                min_time[idx] = min(min_time[idx],cur_time)
                max_time[idx] = max(max_time[idx],cur_time)
                if cores[idx][core] == 0 :
                    cores[idx][core] = 1

        if datas[-1].split()[2] == "[State":
            number_of_gen[idx]+=int(float(datas[-2].split()[-1]))
            number_of_test[idx]+=int(datas[-2].split()[-4])    
        else: 
            number_of_gen[idx]+=int(float(datas[-1].split()[-1]))
            number_of_test[idx]+=int(datas[-1].split()[-4])    
    
    infos = [min_time,max_time,number_of_gen,number_of_test, cores]
    return infos

def get_bug_status(bugs):
    count = [0 for i in range(26)]
    status = ["X" for i in range(26)]
    bug_type = ["soundness" for i in range(0,13)]+["invalid" for i in range(9)]+["crash" for i in range(4)]

    for b in bugs:
        bug_info = b.split('/')
        seed = bug_info[-2].split('.')[0]+".smt2"
        type = bug_info[-3].split('_')[1].lower()
        idx = int(bug_info[-2].split('.')[0].split('_')[1])
        if seed==bug_info[-1] or bug_type[idx] != type:
            continue
        count[idx]+=1
        status[idx] = "O"

    return count,status

def transform_second(time):
    seconds = ""
    s = int(time.seconds)

    seconds = str(s)

    return seconds

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


def print_bug_details_bench(count_bugs,core_infos):
    return

def print_bug_details_v2(status, count_bugs, infos,start,end):
    #[min_time,max_time,number_of_gen,number_of_mutants, cores, number_of_sat_mutants, number_of_unsat_mutants, sat_time, unsat_time, testing_time, gen_time, judge_time]
    print("|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")
    print("| {0:^13} | {1:^12} | {2:^8} | {3:^8} | {4:^9} | {5:^9} | {6:^7} | {7:^7} | {8:^7} | {9:^8} | {10:^10} | {11:^12} | {12:^8} | {13:^10} |".format("Bench_ID","# Reproduced", "Min_Time","Max_Time","# Mutants", "# Gen", "Rate","# SAT","# UNSAT","SAT_TIME","UNSAT_TIME","TESTING_TIME","GEN_TIME","JUDGE_TIME"))
    print("|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")

    min_time, max_time, number_of_gen, number_of_mutants, cores, number_of_sat_mutants, number_of_unsat_mutants, sat_time, unsat_time, testing_time, gen_time, judge_time = infos
    for idx in range(start,end+1):
        benchmark = "bench_"+str(idx)+".smt2"
        reproduced = "0" if count_bugs[idx] == 0 else str(count_bugs[idx])
        min_t = "0" if reproduced == "0" else transform_second(min_time[idx])
        max_t = "0" if reproduced == "0" else transform_second(max_time[idx])
        mutants = number_of_mutants[idx]
        gen = number_of_gen[idx]
        rate = round((float(mutants)/float(gen))*100.0,2) if gen != 0 else "0"
        sat = number_of_sat_mutants[idx]
        unsat = number_of_unsat_mutants[idx]
        st = round(float(sat_time[idx]),2)
        ut = round(float(unsat_time[idx]),2)
        tt = round(float(testing_time[idx]),2)
        gt = round(float(gen_time[idx]),2)
        jd = round(float(judge_time[idx]),2)
        print("| {0:^13} | {1:^12} | {2:^8} | {3:^8} | {4:^9} | {5:^9} | {6:^7} | {7:^7} | {8:^7} | {9:^8} | {10:^10} | {11:^12} | {12:^8} | {13:^10} |".format(benchmark,reproduced,min_t,max_t,mutants,gen,rate,sat,unsat,st,ut,tt,gt,jd))
    print("|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")
    return

def print_bug_details_v3(status,count_bugs, infos,start,end):
    #[min_time,max_time,number_of_gen,number_of_mutants, cores, number_of_sat_mutants, number_of_unsat_mutants, sat_time, unsat_time, testing_time, gen_time, judge_time]
    print("|--------------------------------------------------------------------------------------|")
    print("| {0:^13} | {1:^12} | {2:^8} | {3:^8} | {4:^9} | {5:^9} | {6:^7} |".format("Bench_ID","# Reproduced", "Min_Time","Max_Time","# Mutants", "# Gen", "Rate"))
    print("|--------------------------------------------------------------------------------------|")

    min_time, max_time, number_of_gen, number_of_mutants, cores, number_of_sat_mutants, number_of_unsat_mutants, sat_time, unsat_time, testing_time, gen_time, judge_time = infos
    for idx in range(start,end+1):
        benchmark = "bench_"+str(idx)+".smt2"
        reproduced = "0" if count_bugs[idx] == 0 else str(count_bugs[idx])
        min_t = "0" if reproduced == "0" else transform_second(min_time[idx])
        max_t = "0" if reproduced == "0" else transform_second(max_time[idx])
        mutants = number_of_mutants[idx]
        gen = number_of_gen[idx]
        rate = round((float(mutants)/float(gen))*100.0,2) if gen != 0 else "0"
        sat = number_of_sat_mutants[idx]
        unsat = number_of_unsat_mutants[idx]
        st = round(float(sat_time[idx]),2)
        ut = round(float(unsat_time[idx]),2)
        tt = round(float(testing_time[idx]),2)
        gt = round(float(gen_time[idx]),2)
        jd = round(float(judge_time[idx]),2)
        print("| {0:^13} | {1:^12} | {2:^8} | {3:^8} | {4:^9} | {5:^9} | {6:^7} |".format(benchmark,reproduced,min_t,max_t,mutants,gen,rate))
    print("|--------------------------------------------------------------------------------------|")
    find_res = 0
    fail_res = 0
    for idx in range(1,26):
        if status[idx]=="O":
            find_res += 1
        else:
            fail_res += 1
    print("| {0:^8} {1:^3} | {2:^8}: {3:^3} | {4:^8}: {5:^3} |                                       |".format("Total:",25,"Success:",str(find_res),"Fail:",str(fail_res)))
    print("|--------------------------------------------------------------------------------------|")
    return

def print_bug_details(count_bugs, infos):
    print("|-------------------------------------------------------------------------------------------------------------------------------------------------|")
    print("|   Benchmark_ID  |  # Reproduced  |  Min_Time(s) (30 running) | Max Time(s) (30 running) |  # Mutants  |    # Gen    |  Rate (%)  |  # Runnings  |")
    print("|-------------------------------------------------------------------------------------------------------------------------------------------------|")

    # infos = [min_time,max_time,number_of_gen,number_of_test]
    min_time = infos[0]
    max_time = infos[1]
    number_of_gen = infos[2]
    number_of_test = infos[3]
    cores = infos[4]

    for idx in range(1,26):
        benchmark = "bench_"+str(idx)+".smt2"
        reproduced = "-" if count_bugs[idx] == 0 else str(count_bugs[idx])
        min_t = "-" if reproduced == "-" else transform_second(min_time[idx])
        max_t = "-" if reproduced == "-" else transform_second(max_time[idx])
        mutants = number_of_test[idx]
        gen = number_of_gen[idx]
        rate = round((float(mutants)/float(gen))*100.0,2) if gen != 0 else "-"
        runs = 0
        for i in range(30):
            runs+=cores[idx][i+1]

        print("|  {0:^13}  |  {1:^12}  |  {2:^23}  |  {3:^22}  |  {4:^9}  |  {5:^9}  |  {6:^8}  |  {6:^10}  |".format(benchmark,reproduced,min_t,max_t,mutants,gen,str(rate),str(runs)))
    print("|-------------------------------------------------------------------------------------------------------------------------------------------------|")
    return

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, help = "path of directory")
    parser.add_argument("--detail", type=str, default="false")
    #parser.add_argument("--bench", type=str, default="ALL")
    parser.add_argument("--start",type=int,default=1)
    parser.add_argument("--end",type=int,default=25)
    args = parser.parse_args()

    path = args.input
    detail = args.detail

    logs = get_logs(path)
    bugs = get_bugs(path)

    count_bugs, status_bugs = get_bug_status(bugs)

    if detail == "true":
        infos, core_infos = make_statistics(logs)
        print_bug_details_v3(status_bugs,count_bugs,infos,args.start,args.end)
    elif detail == "debug":
        infos, core_infos = make_statistics(logs)
        print_bug_details_v2(status_bugs,count_bugs,infos,args.start,args.end)
    else:
        print_bug_status(status_bugs)
    return

if __name__=='__main__':
    main()

