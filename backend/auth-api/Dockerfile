FROM python:3.13-slim

WORKDIR /app

COPY /auth-api/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY auth-api /app

COPY shared /shared

RUN pip install --no-cache-dir -e /shared

EXPOSE 8000

CMD ["python", "main.py"]