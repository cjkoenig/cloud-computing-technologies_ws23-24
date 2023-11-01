# https://hub.docker.com/_/python
FROM python:3.9

# create app directory
WORKDIR /code

# bundle app source
COPY . .

# install required packages
RUN pip install -r requirements.txt

# our application will listen on port 5000 inside the container
EXPOSE 5000

# run the application
CMD ["python", "app.py"]