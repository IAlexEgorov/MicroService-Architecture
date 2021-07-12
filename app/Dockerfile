FROM python:3

RUN pip install --upgrade pip && \
    pip install Flask prometheus-flask-exporter

COPY . /app

CMD ["python3", "/app/main.py"]

