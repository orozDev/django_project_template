FROM python:3.13-alpine3.21

ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements.txt /app/requirements.txt
COPY . /app
EXPOSE $PORT

RUN adduser --disabled-password app-user
RUN chown -R app-user:app-user /app
RUN chmod -R 777 /app/static
RUN chmod -R 777 /app/media
RUN chown app-user:app-user -R /app/

RUN pip3 install -r requirements.txt

USER app-user
