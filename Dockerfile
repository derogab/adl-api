FROM python:3

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
RUN pip install pipenv

# Copy Pipfile
COPY Pipfile ./

# Install Pipenv
RUN pipenv install

# Copy app 
COPY app.py ./

# Expose port 443
EXPOSE 443

# Environment
ENV FLASK_APP app.py

# Run the app
CMD [ "pipenv", "run", "gunicorn", \
        "-w", "4", \
        "-b", ":443", \
        "--certfile", "/certs/fullchain.pem", \
        "--keyfile", "/certs/privkey.pem", \
        "app:api" ]