FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --default-timeout=120 --retries=5 -r requirements.txt

COPY requests_sender.py .

CMD ["python", "requests_sender.py"]

# Сборка образа:
# docker build -t requests_service:1 .

# Запуск контейнера:
# docker run --rm requests_service:1
