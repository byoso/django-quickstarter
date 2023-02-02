FROM python:3.11-alpine3.17


ENV PYTHONUNBUFFERED 1

WORKDIR /web

# Dependencies for uWSGI
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN apk del .tmp

COPY . .


RUN chmod +x configs/entrypoint.sh
CMD ["sh","configs/entrypoint.sh"]
