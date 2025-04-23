FROM python:3.10-slim

WORKDIR /app

# Install dependencies
RUN apt-get update && \
    apt-get install -y git ffmpeg libsndfile1 && \
    rm -rf /var/lib/apt/lists/*

# Clone repo
RUN git clone https://github.com/nguyenthienhy/F5-TTS-Vietnamese.git && \
    cd F5-TTS-Vietnamese && \
    pip install .
# Clone bigvgan (thật ra là HiFi-GAN, bigvgan là 1 cấu hình)
RUN git clone https://github.com/jik876/hifi-gan.git /bigvgan && \
    pip install /bigvgan

# Copy Flask app và requirements
COPY tts.py .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5006

CMD ["python", "tts.py"]