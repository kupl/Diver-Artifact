# Diver-Artifact
[Diver](https://github.com/kupl/Diver) is a black-box fuzzer for SMT Solvers. This repository contains the artifact for reproducing the experiments
in our paper accepted at ICSE 2023:

* [Diver: Oracle-Guided SMT Solver Testing with Unrestricted Random Mutations](https://drive.google.com/file/d/1Quyz9hq89uZAVT777R7KlktJ2MnY80wC/view?usp=sharing)

## Table of Contents
- [Operating System and Hardware Requirements](#1-operating-system-and-hardware-requirements)
- [Artifact Structure](#2-artifact-structure)
- [Setup](#3-setup)
    * [Basic Testing](#basic-testing)
- [Comparison with Existing Tools (Section IV-B)](#4-comparison-with-existing-tools-section-iv-b)
- [Utility of Diver's Techniques (Section IV-C)](#5-utility-of-divers-techniques-section-iv-c)
- [Instructions for Extending or Reusing Diver](#6-instructions-for-extending-or-reusing-diver)
    * [Instructions to run Diver on new benchmarks](#instructions-to-run-diver-on-new-benchmarks)
    * [Tool Maintenance](#tool-maintenance)
    
## 1. Operating System and Hardware Requirements
Please see [REQUIREMENTS.md](./REQUIREMENTS.md) for requirements for OS and Hardware environments.

## 2. Artifact Structure

* [Diver](./Diver): contains the implementation of Diver (the same with the one in the docker image that will be installed in [Setup](#3-setup)).
* [Section_IV](./Section_IV): contains benchmark formulas used in our experiments.
* [scripts](./scripts): contains scripts to run experiments and check corresponding results.
* [tests](./tests): contains seed files that will be used for the [basic testing](#basic-testing).

## 3. Setup
Please see [INSTALL.md](./INSTALL.md) for the installation. We provide a dockerized environment for reproducing the experimental results in our paper. 


### Basic Testing
To check whether the installlation was successful or not, run the following commands:
```bash
$ docker create -it --rm -v `pwd`/test_output:/Diver/output --name my_diver jongwook123/diver:icse2023-artifact
$ docker start my_diver
$ docker exec my_diver timeout 20 python3 __main__.py -i tests/seed1.smt2 -l QF_SLIA -s cvc -b /solvers/cvc5-1.0.1/build/bin/cvc5
$ docker exec my_diver mv running_data.log ./output/test_output.log
$ docker rm -f my_diver
```

If the installation and the testing were successful,
you will obtain the log file ```test_output/test_output.log``` that looks similar to the below one:
```
[2023-01-21 10:52:56,059] Start!!!!
[2023-01-21 10:52:57,019] #Mutant 1 #Gen 2.0 Res sat ST 0.0 UT 0.0 TT 0.6809334754943848 GT 0.0009491443634033203 JT 0.1392803192138672
[2023-01-21 10:52:57,134] #Mutant 2 #Gen 3.0 Res sat ST 0.0 UT 0.0 TT 0.7067527770996094 GT 0.002476215362548828 JT 0.22508883476257324
[2023-01-21 10:52:57,425] #Mutant 3 #Gen 7.0 Res sat ST 0.0 UT 0.0 TT 0.7337627410888672 GT 0.004488706588745117 JT 0.4859590530395508
...
```

## 4. Comparison with Existing Tools (Section IV-B)
Please see [SectionIV-B.md](./SectionIV-B.md).

## 5. Utility of Diver's Techniques (Section IV-C)
Please see [SectionIV-C.md](./SectionIV-C.md).

## 6. Instructions for Reusing Diver
Please see [USAGE.md](./USAGE.md) to run Diver on new other formulas.

## 7. Tool Maintenance
Diver will be maintained in a seperate repository: https://github.com/kupl/Diver

