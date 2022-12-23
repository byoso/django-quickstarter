FROM python:3.11-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /www

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

RUN ./manage.py migrate --noinput
RUN ./manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "-w", "3", "project_.wsgi"]
