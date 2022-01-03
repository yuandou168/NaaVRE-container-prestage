FROM continuumio/miniconda3 AS build
RUN apt-get update --allow-releaseinfo-change && apt-get -y install gcc g++
COPY configurations.sp-environment.yaml .
RUN conda env create -f configurations.sp-environment.yaml
RUN conda install -c conda-forge conda-pack
RUN conda-pack -n venv -o /tmp/env.tar && \
    mkdir /venv && cd /venv && tar xf /tmp/env.tar && \
    rm /tmp/env.tar
RUN /venv/bin/conda-unpack

FROM debian:buster AS runtime
COPY --from=build /venv /venv
COPY configurations.sp.py .