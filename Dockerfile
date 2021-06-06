FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y python python-pip
RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT PYTHONPATH=. python3 main.py
