# ADL API
API of the ADL project.

### Build 
```bash
docker build -t derogab/adl-api .
```

### Getting the SSL/TLS certificates
Get a free HTTPS certificate with Let's encrypt using certbot tool. 
> Let's Encrypt is a free, automated, and open certificate authority, run for the public's benefit.
##### Install certbot
```
sudo apt-get install certbot
```
##### Get the certificate
```
sudo certbot certonly -d my-server-domain-name.com -n --standalone
```
The certificate is saved at `/etc/letsencrypt/live/my-server-domain-name.com/fullchain.pem` and the key file at `/etc/letsencrypt/live/my-server-domain-name.com/privkey.pem`.
##### Copy the certificate and set the permissions
```
mkdir /path/to/certs
sudo cp /etc/letsencrypt/live/my-server-domain-name.com/fullchain.pem /path/to/certs/
sudo cp /etc/letsencrypt/live/my-server-domain-name.com/privkey.pem /path/to/certs/
sudo chown $USER:$USER /path/to/certs/*
```
Warning! Let's Encrypt certificates are valid for 90 days. It's necessary to renew the certificates from time to time!

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

---
### ADL Project
This project was developed during the internship period in the university and it was presented as computer science bachelor degree project.

##### Documentation
| | Source |
|:-------------------------:|:-------------------------:|
|Thesis|https://github.com/derogab/adl-thesis|
|Slides|https://github.com/derogab/adl-presentation|

##### Source Code
| | Source |
|:------:|:---------:|
|App|https://github.com/derogab/adl-app|
|Server|https://github.com/derogab/adl-server|
|Api|https://github.com/derogab/adl-api|
