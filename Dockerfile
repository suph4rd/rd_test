FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/rd_test

COPY . /usr/src/rd_test
RUN pip3 install -r /usr/src/rd_test/requirements.txt

EXPOSE 8080