FROM jongwook123/cvc5-1.0.0 as cvc5-1.0.0
FROM jongwook123/cvc5-1.0.1 as cvc5-1.0.1
FROM jongwook123/cvc5-8311316 as cvc5-8311316
FROM jongwook123/cvc5-bf53190 as cvc5-bf53190
FROM jongwook123/cvc5-0bf059f as cvc5-0bf059f
FROM jongwook123/z3-4.11.0 as z3-4.11.0
FROM jongwook123/z3-0146259 as z3-0146259
FROM jongwook123/z3-85fd139 as z3-85fd139
FROM jongwook123/z3-a069b65 as z3-a069b65
FROM jongwook123/z3-506fbf9 as z3-506fbf9
FROM jongwook123/benchmark as benchmark
FROM jongwook123/tools as tools     
FROM ubuntu:20.04 

LABEL maintainer = "Jongwook Kim <jongwook123@korea.ac.kr>"
# Install prerequisites.
ARG MAX_CORE=56
ARG DEBIAN_FRONTEND=noninteractive
USER root
RUN chmod 777 /tmp
RUN apt-get update \
    && apt-get install -y --no-install-recommends apt-utils build-essential git vim cmake g++ m4 openjdk-8-jdk python3.8 python3-pip python3-dev python3-wheel python3-setuptools python-is-python3
WORKDIR /solvers

# Python3 package
RUN pip3 install pyinterval pyparsing toml rstr termcolor numpy pandas antlr4-python3-runtime==4.9.2 ffg pytest Cython scikit-build 


# dReal Install
RUN git clone https://github.com/dreal/dreal4.git dreal-4.21.06.2 && cd dreal-4.21.06.2

# Install prerequisites.
RUN apt-get update \
      && yes "Y" | /solvers/dreal-4.21.06.2/setup/ubuntu/20.04/install_prereqs.sh \
      && rm -rf /var/lib/apt/lists/* \
      && apt-get clean all \
# Build dReal4
      && cd /solvers/dreal-4.21.06.2 \
      && bazel build //:archive \
      && tar xfz bazel-bin/archive.tar.gz --strip-components 3 -C /usr \
# Install Python3 Binding
      && python3 setup.py bdist_wheel \
      && pip3 install ./dist/dreal-*-cp38-none-manylinux1_x86_64.whl \
      && bazel clean --expunge \
# Clean up
      && cd /solvers \
      && rm -rf dreal-4.21.06.2 \
      && rm -rf /root/.cache/bazel \


WORKDIR /solvers
COPY --from=cvc5-1.0.0 /solvers/cvc5-1.0.0 ./cvc5-1.0.0
COPY --from=cvc5-1.0.1 /solvers/cvc5-1.0.1 ./cvc5-1.0.1
COPY --from=cvc5-8311316 /solvers/cvc5-8311316 ./cvc5-8311316
COPY --from=cvc5-bf53190 /solvers/cvc5-bf53190 ./cvc5-bf53190
COPY --from=cvc5-0bf059f /solvers/cvc5-0bf059f ./cvc5-0bf059f
COPY --from=z3-4.11.0 /solvers/z3-4.11.0 ./z3-4.11.0
COPY --from=z3-0146259 /solvers/z3-0146259 ./z3-0146259
COPY --from=z3-85fd139 /solvers/z3-85fd139 ./z3-85fd139
COPY --from=z3-a069b65 /solvers/z3-a069b65 ./z3-a069b65
COPY --from=z3-506fbf9 /solvers/z3-506fbf9 ./z3-506fbf9

RUN cd /solvers/z3-4.11.0 && python3 scripts/mk_make.py --prefix=/usr/local --python --pypkgdir=/usr/local/lib/python3.8/dist-packages && cd build; make -j $MAX_CORE && make install
RUN cd /solvers/cvc5-1.0.1 && ./configure.sh --auto-download --python-bindings && cd build && make -j $MAX_CORE && make install
RUN cd /solvers/cvc5-1.0.0 && ./configure.sh --auto-download --python-bindings && cd build && make -j $MAX_CORE
RUN cd /solvers/cvc5-8311316 && ./configure.sh --auto-download --python-bindings && cd build && make -j $MAX_CORE
RUN cd /solvers/cvc5-bf53190 && ./configure.sh --auto-download --python-bindings && cd build && make -j $MAX_CORE
RUN cd /solvers/cvc5-0bf059f && ./configure.sh --auto-download --python-bindings && cd build && make -j $MAX_CORE


#RUN mkdir /Benchmark
#COPY --from=benchmark /SAT /Benchmark/

RUN mkdir /ex_tools
COPY --from=tools /tools /ex_tools
RUN cd /ex_tools && git clone https://github.com/alebugariu/StringSolversTests.git autostring && cd autostring && git checkout 5451df7579ec47260f7040867ff2a93f2d2a4ab6
RUN cd /ex_tools/storm && python3 setup.py install

# Copy Diver 
RUN cd /
COPY ./Diver /Diver

# Add Scripts and Benchmark
COPY ./scripts /Diver/scripts
COPY ./Section_IV /Diver/Section_IV
COPY ./tests /Diver/tests
WORKDIR /Diver

CMD ["/bin/bash"]
