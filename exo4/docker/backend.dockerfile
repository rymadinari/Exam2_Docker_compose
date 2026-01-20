FROM python:3.10-slim

WORKDIR /app

COPY backend/src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/src .

CMD ["python", "app.py"]
