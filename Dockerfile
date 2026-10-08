# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.12.10
FROM python:${PYTHON_VERSION}-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Application port
EXPOSE 5001

# Start Flask application using Gunicorn
# CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app:app"]
CMD ["python", "app.py"]