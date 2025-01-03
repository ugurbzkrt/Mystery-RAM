FROM python:3.9-slim
WORKDIR /app

COPY cache-b.py /app/cache-b.py


RUN pip install --no-cache-dir psutil

CMD ["python", "cache-b.py"]
