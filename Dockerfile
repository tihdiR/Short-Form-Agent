# Dockerfile

FROM python:3.10-slim

RUN apt-get update && apt-get install -y ffmpeg

WORKDIR /app

# Copy everything into the container
COPY . .

# Install dependencies

RUN pip install --default-timeout=300 yt_dlp && \
    pip install --default-timeout=300 --no-cache-dir -r requirements.txt

# Set default command
CMD ["python", "main.py"]