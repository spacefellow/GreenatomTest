FROM python:3.11-slim

WORKDIR /src

COPY requirements.txt .

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

COPY . /src