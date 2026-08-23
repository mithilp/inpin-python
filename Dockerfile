# Dockerfile
FROM python:3.12.6-bookworm

ENV PYTHONUNBUFFERED True
ENV APP_HOME /
WORKDIR $APP_HOME
COPY . ./

RUN apt-get update && apt-get -y install cmake
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD exe gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app