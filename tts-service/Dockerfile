FROM python:3.10-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    git \
    espeak \
    libsndfile1 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files (Portainer will handle cloning from Git)
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Optional: print installed TTS version for debug
RUN python -c "import TTS; print('Installed Coqui TTS version:', TTS.__version__)"

# Expose the app port
EXPOSE 5006

# Start the app
CMD ["python", "tts.py"]