## nginx-gunicorn-flask

This repository contains files necessary for building a Docker image of
Nginx + Gunicorn + Flask.


### Base Docker Image

* python:3.6


### Installation

1. Install [Docker](https://www.docker.com/).

2. build image

```bash
cd nginx-gunicorn-flask
docker build -t nginx-gunicorn-flask:latest  .
docker pull danriti/nginx-gunicorn-flask
```


### Usage

```bash
docker run -d --name nginx-gunicorn-flask -p 80:80  nginx-gunicorn-flask:latest
```

After few seconds, open `http://<host>` to see the Flask app.
