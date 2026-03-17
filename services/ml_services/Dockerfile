FROM python:3.11-slim

COPY . /ml_service

WORKDIR /ml_service

RUN pip install --no-cache-dir -r requirements.txt

VOLUME ["/models"]

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# docker build -t mobile_price_service:1 .
# docker run -p 8000:8000 -v ${PWD}/../models:/models mobile_price_service:1