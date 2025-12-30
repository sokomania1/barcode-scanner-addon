FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY barcode_scanner_mqtt.py .
CMD ["python", "barcode_scanner_mqtt.py"]
