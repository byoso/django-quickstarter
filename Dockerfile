FROM python:3.11-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /web

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

# RUN ./manage.py migrate --noinput
# RUN ./manage.py collectstatic --noinput

EXPOSE 8000

RUN chmod +x prod_config/entrypoint.sh
CMD ["bash","prod_config/entrypoint.sh"]
