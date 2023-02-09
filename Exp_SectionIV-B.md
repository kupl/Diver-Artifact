# Comparison with Existing Tools (Section IV-B)
## Table IV
To reproduce the results in Table IV, run the following commands. Please note that running each command will take quite a long time (**about 25h for each tool** - 1h for each benchmark * 25 benchmarks). As an exception, runnning autostring will take less than 16h.

```bash
$ python3 scripts/table_IV_run.py --tool typefuzz --core 30 --time 3600 
$ python3 scripts/table_IV_run.py --tool opfuzz --core 30 --time 3600
$ python3 scripts/table_IV_run.py --tool storm --core 30 --time 3600
$ python3 scripts/table_IV_run.py --tool autostring --core 30 --time 3600 
$ python3 scripts/table_IV_run.py --tool fusion --core 30 --time 3600 
```
* ```[tool]```: the name of a compared testing tool: {typefuzz, opfuzz, storm, autostring, fusion}.
* ```[core]```: the number of cores to be used for parallel executions (default: 30). One execution (core) corresponds to one repetition.
* ```[time]```: the timeout (in seconds) for each benchmark (default: 3600).

Once each command finishes, the directory ```./output/<tool_name>``` will be generated.
To check the bug-finding results, run the following commands (each command will take at most **10 minutes**):
```
$ python3 scripts/table_IV_plot.py --input output/typefuzz
$ python3 scripts/table_IV_plot.py --input output/opfuzz
$ python3 scripts/table_IV_plot.py --input output/storm
$ python3 scripts/table_IV_plot.py --input output/autostring
$ python3 scripts/table_IV_plot.py --input output/fusion
```

**Note: Version of Compared Tools**
* The 5 compared tools used for the experiments are the latest versions as of August 2022: 
  + TypeFuzz([8798c89](https://github.com/testsmt/yinyang/tree/8798c89ace78fad5617323e61ba8f0a7e3c59f16)), OpFuzz([8798c89](https://github.com/testsmt/yinyang/tree/8798c89ace78fad5617323e61ba8f0a7e3c59f16)), Storm([55d0916](https://github.com/Practical-Formal-Methods/storm/tree/55d091624523a0544112ffc339fe81103b3daa2b)), AutoString([5451df7](https://github.com/alebugariu/StringSolversTests/tree/5451df7579ec47260f7040867ff2a93f2d2a4ab6)) and Fusion([8798c89](https://github.com/testsmt/yinyang/tree/8798c89ace78fad5617323e61ba8f0a7e3c59f16)).

**Note: Running experiments using a machine with fewer than 30 cores**

For example, if your machine has 16 cores in total and you wish to use 10 cores only,
run the following commands to repeat executions of each tool 30 times. Note that, in this case, the running time will be **about 75h for each tool** (1h for each benchmark * 25 benchmakrs * 3 commands for each tool). As an exception, runnning autostring will take less than 48h.
```
$ python3 scripts/table_IV_run.py --tool typefuzz --core 10 --time 3600 
$ python3 scripts/table_IV_run.py --tool typefuzz --core 10 --time 3600
$ python3 scripts/table_IV_run.py --tool typefuzz --core 10 --time 3600
$ python3 scripts/table_IV_run.py --tool opfuzz --core 10 --time 3600
$ python3 scripts/table_IV_run.py --tool opfuzz --core 10 --time 3600
$ python3 scripts/table_IV_run.py --tool opfuzz --core 10 --time 3600
...
$ python3 scripts/table_IV_run.py --tool fusion --core 10 --time 3600 
$ python3 scripts/table_IV_run.py --tool fusion --core 10 --time 3600
$ python3 scripts/table_IV_run.py --tool fusion --core 10 --time 3600
```

The bug-finding results can be obtained by the above commands that start with ``python3 scripts/table_IV_plot.py``.


## Robustness of Diver
To reproduce the results in the paragraph ***Robustness of Diver***,  run the following command. Please note that running the command will take quite a long time (**about 25h** - 1h for each benchmark * 25 benchmarks).
```
$ python3 scripts/diver_run.py --mode diver --core 30 --time 3600  
```
* ```[core]```: the number of cores to be used for parallel executions (default: 30). One execution (core) corresponds to one repetition.
* ```[time]```: the timeout (in seconds) for each benchmark (default: 3600).

Once the execution finishes, the directory ```./output/diver``` will be generated. You can check the bug-finding results as follows:
```
$ python3 scripts/diver_plot.py --input output/diver --detail true
```

**Note: Running experiments using a machine with fewer than 30 cores**

For example, if your machine has 16 cores in total and you wish to use 10 cores only,
run the following commands to repeat executions of Diver 30 times.
Note that, in this case, the running time will be **about 75h** (1h for each benchmark * 25 benchmakrs * 3 commands).
```
$ python3 scripts/table_IV_run.py --tool diver --core 10 --time 3600 
$ python3 scripts/table_IV_run.py --tool diver --core 10 --time 3600
$ python3 scripts/table_IV_run.py --tool diver --core 10 --time 3600
```

The bug-finding results can be obtained by the above command that starts with ``python3 scripts/diver_plot.py``.



### Structure of Outputs
The structure of the directory ```output``` is as follows:
```text
output
└── diver : contains raw data produced by Diver.
      ├── run_1: contains results from the 1st execution.
      │      ├── <benchmark_name>: includes the log file/bug directory generated by Diver on <benchmark_name>.smt2.
      │      │    │
      │      │    ├── <benchmark_name>.log: the file which records the Diver's running status on <benchmark_name>.smt2.
      │      │    │
      │      │    └── bug: contains seed formulas and bug-triggering formulas detected by Diver.
      │      ...
      ├── run_2: contains results from the 2nd execution.
      ... 
```
For example, suppose Diver found a soundness bug in CVC5 by mutating the seed formula ```bench_1.smt2```, during the execution at a certain core (namely ``run_1``). Then, the seed and the bug-triggering mutant formula will be stored in the ```output/diver/run_1/bench_1/bug/cvc_soundness/bench_1.smt2_<RANDOM_NUMBER>```. 

## Finding Bugs Detected by Existing Work
To reproduce the the experimental result of the paragraph ***Finding Bugs Detected by Existing Work***,
run the following command. Please note that the command will take about 2h (1h for each benchmark * 2 benchmarks). 
```
$ python3 scripts/reproduce_storm_run.py --core 30 --time 3600  
```
* ```[core]```: the number of cores to be used for parallel executions (default: 30). One execution (core) corresponds to one repetition.
* ```[time]```: the timeout (in seconds) for each benchmark (default: 3600).

Once terminated, run the following command to check the bug-finding results:
```
$ python3 scripts/reproduce_storm_plot.py --input output/reproduce_storm
```

**Note: Running experiments using a machine with fewer than 30 cores**

For example, if your machine has 16 cores in total and you wish to use 10 cores only,
run the following commands to repeat executions of Diver 30 times.
Note that, in this case, the running time will be **about 6h** (1h for each benchmark * 2 benchmakrs * 3 commands).
```
$ python3 scripts/reproduce_storm_run.py --core 10 --time 3600
$ python3 scripts/reproduce_storm_run.py --core 10 --time 3600
$ python3 scripts/reproduce_storm_run.py --core 10 --time 3600
```

The bug-finding results can be obtained by the above command that starts with ``python3 scripts/reproduce_storm_plot.py``.
