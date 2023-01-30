FROM python:3.11-slim-buster
# FROM python:alpine3.17

ENV PYTHONUNBUFFERED 1

WORKDIR /web

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000


RUN chmod +x configs/entrypoint.sh
CMD ["bash","configs/entrypoint.sh"]
