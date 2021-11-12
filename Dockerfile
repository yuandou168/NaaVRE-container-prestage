
FROM continuumio/miniconda3 AS build
RUN apt-get update --allow-releaseinfo-change && apt-get -y install gcc g++
RUN ls
