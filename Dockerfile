FROM python:3
MAINTAINER Joao Castro

ENV CODE_PATH /usr/src/kittens
WORKDIR $CODE_PATH

RUN apt-get update && apt-get install -qq -y \
    build-essential libpq-dev --no-install-recommends

COPY ./app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD gunicorn -b 0.0.0.0:80 --access-logfile - "app.kittens:app"
