import argparse
import os, sys
import subprocess
import shutil
import time
import logging
from logging.config import dictConfig


def get_logic():
    ###Logic for benchmark (Table4 - Logic)
    logic = ["QF_SLIA" for i in range(25)]
    logic[3] = "QF_NRA"
    logic[7] = "QF_NRA"
    logic[8] = "QF_NRA"
    logic[9] = "QF_NRA"
    logic[10] = "QF_NRA"
    logic[11] = "QF_NRA"
    logic[18] = "QF_LIA"
    logic[20] = "QF_NIA"
    logic[21] = "QF_LIA"
    return logic

def get_opt():
    ###Option of SMT Solver for benchmark (Table IV)
    opt = [None for i in range(25)]
    opt[1] = "--sygus-inst"
    opt[4] = "smt.string_solver=z3str3"
    opt[5] = "smt.string_solver=z3str3"
    opt[6] = "smt.string_solver=z3str3"
    opt[9] = "rewriter.flat=false"
    opt[12] = "--strings-deq-ext"
    opt[13] = "--sygus-inst"
    opt[14] = "--no-strings-lazy-pp"
    opt[15] = "--sygus-rr-synth-input,--incremental"
    opt[16] = "--sygus-inst"
    opt[17] = "--sygus-inst"
    opt[19] = "smt.string_solver=z3str3"
    opt[20] = "smt.arith.solver=2"
    opt[21] = "--sygus-inst"
    opt[22] = "--sygus-inst"
    opt[23] = "--strings-deq-ext"
    opt[24] = "--strings-fmf"
    return opt


def get_solverbin():
    ###Path of SMT Solver binary for benchmark Table4 - Solver
    cvc5_v0 = "/solvers/cvc5-1.0.0/build/bin/cvc5"

    cvc5_v1 = "/solvers/cvc5-1.0.1/build/bin/cvc5"
    cvc5_bench_13 = "/solvers/cvc5-8311316/build/bin/cvc5"
    cvc5_bench_17 = "/solvers/cvc5-bf53190/build/bin/cvc5"
    cvc5_bench_18 = "/solvers/cvc5-0bf059f/build/bin/cvc5"
    z3 = "/solvers/z3-4.11.0/build/z3"
    dreal = "dreal"

    solverbin = [cvc5_v1,cvc5_v1,cvc5_v0,cvc5_v0,z3,z3,z3,z3,z3,z3,dreal,dreal,cvc5_bench_13,cvc5_v1,cvc5_v0,cvc5_v0,cvc5_bench_17,cvc5_bench_18,cvc5_v0,z3,z3,cvc5_v1,cvc5_v1,cvc5_v1,cvc5_bench_18]
    return solverbin

def diver(benchmark,solver,solverbin,opt,logic,solver_api,timeout,mode,solver_time):
    default_cmd = " --max_depth=5 --mutants=1000 --timeout="+str(solver_time)+" --opt=True --mode="+mode
    #for i in range(25):
    if solver == "cvc":
        os.system("rm -rf /usr/local/lib/python3.8/dist-packages/cvc5*")
        solver_dir = '/'.join(solverbin.split('/')[:-2])
        os.system("make -C "+solver_dir+" install >> null")

    cmd = "timeout "+timeout+" python3 __main__.py --solver="+solver+" --solverapi="+solver_api+" --solverbin="+solverbin+" --benchmark=./tmp_bench/"+benchmark+" --logic="+logic+default_cmd
    if benchmark == "bench_19.smt2":
        cmd = cmd+ " --experiment=1"
    if opt is not None:
        cmd = cmd+" --option="+opt

    print(cmd)
    os.system(cmd)
    shutil.move("./running_data.log","./output/"+benchmark.split('.')[0]+".log")
    shutil.rmtree("./tmp_benchmark")
    shutil.rmtree("./test_suit")

    ## Bug Type 
    if os.path.exists("./bug_dir"):
        shutil.move("./bug_dir","./output/bug")
    return

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', type=str, help = 'the variant of Diver for experiment, mode = [diver,noweight,nocomp]', default="diver")
    parser.add_argument('--time', type=int, help = 'timeout(s) for each benchmark', default=3600)
    parser.add_argument("--benchmark", type=str)
    parser.add_argument('--solver_time', type=int, help = 'timeout(s) for SMT solver', default=10)
    args = parser.parse_args()

    shutil.copytree("./Section_IV/Benchmark_Table_IV/", "./tmp_bench")
    if not os.path.exists("./output"):
        os.mkdir("./output")

    benchmark = ["bench_"+str(i)+".smt2" for i in range(1,26)]
    solver = ["cvc" for i in range(4)]+["z3" for i in range(6)]+["dreal" for i in range(2)]+["cvc" for i in range(7)]+["z3" for i in range(2)]+["cvc" for i in range(4)]
    solver_api = ["cvc" for i in range(3)]+["z3" for i in range(7)]+["dreal" for i in range(2)]+["cvc" for i in range(7)]+["z3" for i in range(2)]+["cvc" for i in range(4)]
    
    opt = get_opt()
    logic = get_logic()
    solverbin = get_solverbin()
    idx = int(((args.benchmark).split('.')[0]).split('_')[-1])-1
    ## Run Diver
    diver(args.benchmark,solver[idx],solverbin[idx],opt[idx],logic[idx],solver_api[idx],str(args.time),args.mode,args.solver_time)
    return

if __name__=='__main__':
    main()