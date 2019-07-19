# celiAI
Small project for classifying salsa and merengue songs using Deep Learning

# Setup instructions

1. Clone repo
2. Go to /celiaAI and build the container using the Dockerfile:
```
docker build -t celiai .
```
3. Run the docker containing and map the volumes:
```
docker run -it --name celiai_img -v /path/to/celiAI/:/celiAI/ -p 8888:8888 celiai
```

# Running Jupyter Notebook in container
1. Activate fastai environment:
```
conda activate fastai
```
2. Run jupyter notebook:
```
jupyter notebook --ip 0.0.0.0 --no-browser --allow-root
```
3. On your host go to `localhost:8888/` and introduce the  required token