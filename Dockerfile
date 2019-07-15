FROM continuumio/miniconda3

RUN mkdir /celiAI
WORKDIR /celiAI

ADD requirements.txt /celiAI/

RUN apt-get update && apt-get install -y --no-install-recommends \
    nano \
    sudo \
    python-pip \
    gnupg \
    ffmpeg
RUN conda config --append channels conda-forge
RUN conda config --append channels pytorch
RUN conda config --append channels fastai
RUN conda create --name celiai --file requirements.txt
RUN echo "source activate celiai" > ~/.bashrc
ENV PATH /opt/conda/envs/celiai/bin/:$PATH
ENV PYTHONPATH /celiAI:$PYTHONPATH
ENV CELIAI /celiAI