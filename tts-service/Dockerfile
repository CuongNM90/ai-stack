# Use Python slim image
FROM python:3.10-slim

# Install required system packages
RUN apt-get update && apt-get install -y \
    git \
    espeak \
    libsndfile1 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy your TTS server script
COPY tts.py .

# Install the latest Coqui TTS and dependencies
RUN pip install --upgrade pip
RUN pip install TTS

# Pre-download Vietnamese model (optional but recommended for speed)
RUN python -c "from TTS.api import TTS; TTS.from_pretrained('tts_models/vi/vivos/glow-tts')"

# Expose the port
EXPOSE 5006

# Run the TTS app
CMD ["python", "tts.py"]