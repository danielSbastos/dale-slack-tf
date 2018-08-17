FROM python:3.6-slim

RUN apt-get update

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

CMD python3.6 app.py
