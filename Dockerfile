FROM continuumio/miniconda3

RUN mkdir /celiAI
WORKDIR /celiAI

ADD requirements.txt /celiAI/

RUN apt-get update && apt-get install -y --no-install-recommends \
    nano \
    sudo \
    build-essential \
    python-pip \
    gnupg \
    ffmpeg \
#    libssl-dev \
    python3-dev \
    gcc

RUN conda config --append channels conda-forge
RUN conda create --name fastai
RUN echo "source activate fastai"
RUN pip install cython && \
    pip install https://download.pytorch.org/whl/cpu/torch-1.1.0-cp37-cp37m-linux_x86_64.whl && \
    pip install https://download.pytorch.org/whl/cpu/torchvision-0.3.0-cp37-cp37m-linux_x86_64.whl && \
    pip install fastai && \
    pip install jupyter notebook && \
    pip install jupyter_contrib_nbextensions
RUN conda create --name celiai --file requirements.txt
ENV PATH /opt/conda/envs/celiai/bin/:/opt/conda/envs/fastai/bin/:$PATH
ENV PYTHONPATH /celiAI:$PYTHONPATH
ENV CELIAI /celiAI