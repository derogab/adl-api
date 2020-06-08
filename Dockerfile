FROM python:3

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
RUN pip install flask

# Copy app 
COPY app.py ./

# Run the app
ENTRYPOINT [ "python", "./app.py" ]
CMD []