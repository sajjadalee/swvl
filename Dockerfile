FROM python:3.7.2

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir swvl_app

COPY . /swvl_app

WORKDIR /swvl_app




