FROM python:3.10-slim

# Avoid interactive tzdata install
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

# Install dependencies
RUN apt-get update && \
    apt-get install -y libsndfile1 ffmpeg git && \
    rm -rf /var/lib/apt/lists/*

# Install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY app.py .

EXPOSE 5006

CMD ["python", "tts.py"]
