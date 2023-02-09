# Utility of Our Techniques (Section IV-C) 
## Figure 3
To reproduce the results in Figure 3, run the following commands. Please note that running each command will take quite a long time (**about 25h for each command** - 1h for each benchmark * 25 benchmarks).
```
$ python3 scripts/diver_run.py --mode noweight --core 30 --time 3600
$ python3 scripts/diver_run.py --mode nocomp --core 30 --time 3600
```
* ```[core]```: the number of cores to be used for parallel executions (default: 30). One execution (core) corresponds to one repetition.
* ```[time]```: the timeout (in seconds) for each benchmark (default: 3600).


Then, run the following commands for visualizing the corresponding results:
```
$ python3 scripts/diver_plot.py --input output/diver_noweight --detail true
$ python3 scripts/diver_plot.py --input output/diver_nocomp --detail true
```

**Note: Running experiments using a machine with fewer than 30 cores**

For example, if your machine has 16 cores in total and you wish to use 10 cores only,
run the following commands to repeat executions of each mode 30 times.
Note that, in this case, the running time for each mode will be **about 75h** (1h for each benchmark * 25 benchmakrs * 3 commands for each mode).
```
$ python3 scripts/diver_run.py --mode noweight --core 10 --time 3600
$ python3 scripts/diver_run.py --mode noweight --core 10 --time 3600
$ python3 scripts/diver_run.py --mode noweight --core 10 --time 3600
$ python3 scripts/diver_run.py --mode nocomp --core 10 --time 3600
$ python3 scripts/diver_run.py --mode nocomp --core 10 --time 3600
$ python3 scripts/diver_run.py --mode nocomp --core 10 --time 3600
```

The bug-finding results can be obtained by the above commands that start with ``python3 scripts/diver_plot.py``.
