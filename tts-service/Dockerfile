FROM python:3.10-slim

WORKDIR /app

# Install dependencies
RUN apt-get update && \
    apt-get install -y git ffmpeg libsndfile1 && \
    rm -rf /var/lib/apt/lists/*

# Clone repo
RUN git clone https://github.com/hynt-h/f5-tts.git && \
    cd f5-tts && \
    pip install .

# Copy Flask app
COPY tts.py .
COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 5006

CMD ["python", "tts.py"]
