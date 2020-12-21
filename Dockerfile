FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/rd_test

COPY ./requirements.txt /usr/src/rd_test/requirements.txt
RUN pip3 install -r /usr/src/rd_test/requirements.txt

COPY . /usr/src/rd_test

EXPOSE 8080
