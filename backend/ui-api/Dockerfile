FROM python:3.12-slim

WORKDIR /app

COPY /ui-api/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ui-api /app

COPY shared /shared

RUN pip install --no-cache-dir -e /shared

EXPOSE 8001

CMD ["python", "main.py"]