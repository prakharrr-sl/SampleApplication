FROM ubuntu:latest
MAINTAINER Prakhar Rawat "prakhar.rawat@saucelabs.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

#source files
COPY . /app
ENV HOME=/app
WORKDIR /app

RUN pip install -r requirements.txt

ENV FLASK_APP = app.py

EXPOSE 5000

#ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:5000", "-w", "wsgi:app"]
