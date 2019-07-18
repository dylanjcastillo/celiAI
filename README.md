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
