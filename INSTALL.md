# Installation

## Docker Images
We have packaged our artifacts in a Docker image containing all resources to reproduce the results of our paper. We have already setup all the environment to run the tool in the image. The following command will load the docker image name ```jongwook123/diver:icse2023-artifact``` (this takes **~5 min**):
```
$ docker pull jongwook123/diver:icse2023-artifact
```

We provide the additional Docker image for reproducing the results of [AutoString](https://github.com/alebugariu/StringSolversTests) we used in the paper. Before running the comparison experiment, you need to import the image using the following script:
```
$ docker pull jongwook123/diver-artifact-autostring-icse2023:icse
```

## Python library
```
$ pip3 install pandas z3-solver
```
