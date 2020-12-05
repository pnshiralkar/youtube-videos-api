FROM python:3-alpine

COPY src/requirements.txt /app/

WORKDIR /app/

RUN pip3 install -r requirements.txt

COPY src /app/