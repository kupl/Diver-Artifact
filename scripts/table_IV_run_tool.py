import os,sys
import argparse
import shutil

TOOL = ""
TIEMOUT = "0"
MUTANTS = 0

def get_tool_path():
    path = ""
    if TOOL == "typefuzz":
        path = "/ex_tools/yinyang/bin/typefuzz"
    elif TOOL == "opfuzz":
        path = "/ex_tools/yinyang/bin/opfuzz"
    elif TOOL == "storm":
        path = "/ex_tools/storm/storm/__main__.py"
    elif TOOL == "autostring":
        path = ""
    elif TOOL == "fusion":
        path = "/ex_tools/yinyang/bin/yinyang"
    else:
        raise Exception("Line-19: Unsupported TOOL {}".format(TOOL))

    return path


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
    opt = ["" for i in range(25)]
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

def setup_globals(tool,timeout,mutants):
    global TOOL 
    global TIMEOUT
    global MUTANTS

    TIMEOUT = str(timeout)
    TOOL = tool
    MUTANTS = mutants

def get_diff_solver(solver, option, solverbin,logic):
    solvers = ""
    if solver == "z3":
        solvers = solverbin+" "+option+" model_validate=true smt.logic="+logic
        solvers = "/solvers/cvc5-1.0.1/build/bin/cvc5 --check-models --force-logic="+logic+";"+solvers
    elif solver == "cvc":
        solvers = solverbin+" "+option+" --check-models --force-logic="+logic
        solvers = "/solvers/z3-4.11.0/build/z3 model_validate=true smt.logic="+logic+";"+solvers
    elif solver == "dreal":
        solvers = "/solvers/cvc5-1.0.1/build/bin/cvc5 --check-models --force-logic="+logic+";"+solverbin
    else:
        raise Exception("Line-19: Unsupported TOOL {}".format(TOOL))
    return solvers


def get_cmd(tool_path,solver,option,solverbin,benchmark,logic,solver_time):
    cmd = ""
    bench = benchmark.split('/')[-1].split('.')[0]
    if TOOL == "typefuzz" or TOOL == "opfuzz":
        option = ' '.join(option.split(','))
        diff_solvers = get_diff_solver(solver,option,solverbin,logic)
        cmd = "timeout "+TIMEOUT+" "+tool_path+' "'+diff_solvers+'" '+benchmark+" -t "+str(solver_time)+" -i "+str(MUTANTS)+" -l ./output/log -b ./output/bug"
    elif TOOL == "storm":
        cmd_mk = "mkdir -p ./tmp/"+logic
        os.makedirs("./tmp/"+logic, exist_ok=True)
        shutil.copy(benchmark,"./tmp/"+logic+"/test.smt2")
        if len(option)==0:
            cmd = "timeout "+TIMEOUT+" python3 "+tool_path+" --benchmark=./tmp --solverbin="+solverbin+" --solver="+solver+" --theory="+logic
        else:
            cmd = "timeout "+TIMEOUT+" python3 "+tool_path+" --benchmark=./tmp --solverbin="+solverbin+" --solver="+solver+" --theory="+logic+" --opt="+option
        cmd = cmd +" > ./output/"+bench+".log"
    elif TOOL == "autostring":
        cmd = ""
    elif TOOL == "fusion":
        option = ' '.join(option.split(','))
        solvers = solverbin
        if solver == "z3":
            solvers = solvers+" model_validate=true smt.logic="+logic
        elif solver == "cvc":
            solvers = solvers+" --check-models --force-logic="+logic        
        cmd = "timeout "+TIMEOUT+" "+tool_path+" -o sat"+' "'+solvers+'" '+benchmark+" "+benchmark+" -t "+str(solver_time)+" -i"+str(MUTANTS)+" -l ./output/log -b ./output/bug"
    else:
        raise Exception("Line-19: Unsupported TOOL {}".format(TOOL))
    
    return cmd

def run(tool_path,logic,option,solverbin,solver,benchmark,solver_time):
    cmd = get_cmd(tool_path, solver, option, solverbin, benchmark, logic, solver_time)
    print(cmd)
    os.system(cmd) 
    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tool", type=str, help = "e.g., typefuzz, opfuzz, strom, autostring and fusion.")
    parser.add_argument("--time", type=int, default = 3600)
    parser.add_argument("--mutants", type=int, default = 2000000)
    parser.add_argument("--benchmark", type=str)
    parser.add_argument('--solver_time', type=int, help = 'timeout(s) for SMT solver', default=10)
    os.makedirs("./output", exist_ok=True)
    args = parser.parse_args()

    tool = args.tool
    timeout = args.time
    benchmark = args.benchmark
    setup_globals(tool, timeout,args.mutants)

    idx = int((benchmark.split('.')[0]).split('_')[-1])
    shutil.copytree("./Section_IV/Benchmark_Table_IV/", "./tmp_bench")
    #benchmark = ["./tmp_bench/bench_"+str(i)+".smt2" for i in range(1,26)]
    solver = ["cvc" for i in range(4)]+["z3" for i in range(6)]+["dreal" for i in range(2)]+["cvc" for i in range(7)]+["z3" for i in range(2)]+["cvc" for i in range(4)]
    tool_path = get_tool_path()
    logic = get_logic()
    option = get_opt()
    solverbin = get_solverbin()
    
    run(tool_path,logic[idx-1],option[idx-1],solverbin[idx-1],solver[idx-1],"./tmp_bench/"+benchmark,args.solver_time)
    
if __name__ == "__main__":
    main()