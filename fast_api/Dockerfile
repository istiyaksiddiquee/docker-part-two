FROM python:3.10-alpine3.16

ARG PORT
ENV PORT=$PORT

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./codebase/ /usr/src/app

EXPOSE $PORT