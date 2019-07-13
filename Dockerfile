FROM continuumio/miniconda3

RUN mkdir /celiAI
WORKDIR /celiAI

ADD requirements.txt /celiAI/

RUN apt-get update && apt-get install -y --no-install-recommends \
    nano \
    sudo \
    python-pip \
    gnupg

RUN conda env create --name celiai --file requirements.txt --channel conda-forge
RUN echo "source activate celiai" > ~/.bashrc
ENV PATH /opt/conda/envs/celiai/bin/:$PATH
ENV PYTHONPATH /celiAI:$PYTHONPATH
ENV CELIAI /celiAI