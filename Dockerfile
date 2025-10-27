FROM python:3.10-slim

WORKDIR /app

# system deps for pdfplumber and pdf handling (pdfplumber relies on Pillow and some system libs)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpoppler-cpp-dev \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app /app

ENV DATA_DIR=/app/data
RUN mkdir -p /app/data

EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "--workers", "2"]
