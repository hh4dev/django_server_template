FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /src
WORKDIR /src
ADD requirements.txt /src/
RUN apk add --no-cache build-base mariadb-connector-c-dev
RUN pip install -r requirements.txt
ADD . /src/