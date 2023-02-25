FROM python:3.10
WORKDIR /api

COPY . .
RUN pip install -r requirements.txt