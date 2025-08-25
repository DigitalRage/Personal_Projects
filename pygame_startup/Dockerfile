# Use the official Python devcontainer image
FROM mcr.microsoft.com/devcontainers/python:3.11

# Install PyGame system dependencies
RUN apt-get update && \
    apt-get install -y \
      libsdl2-dev \
      libsdl2-image-dev \
      libsdl2-mixer-dev \
      libsdl2-ttf-dev \
      libportmidi-dev \
      libfreetype6-dev \
      xvfb && \
    rm -rf /var/lib/apt/lists/*