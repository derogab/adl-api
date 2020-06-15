# ADL API
API of the ADL project.

### Build 
```bash
docker build -t derogab/adl-api .
```

### Run 
```bash
docker run \
    -dit \
    -p 443:443 \
    --name adl-api \
    --restart=always \
    --mount type=bind,source=/path/to/certs,target=/certs \
    derogab/adl-api
```

### Utils
- [Deploying a Flask application with Gunicorn and Docker](https://medium.com/trabe/deploying-a-flask-application-with-gunicorn-and-docker-2bc7c4c10dd4)
