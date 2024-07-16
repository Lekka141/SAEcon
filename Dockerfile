# Use the official Python image from Docker Hub
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies required for Python packages like pandas
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libc-dev \
    libpq-dev \
    python3-distutils \
    python3-apt \
    build-essential \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install distutils using ensurepip
RUN python3 -m ensurepip --upgrade

# Upgrade pip, setuptools, and wheel to specific versions
RUN pip install --upgrade pip setuptools==57.5.0 wheel

# Copy the requirements.txt into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy the rest of your application code to the container
COPY . .

# Expose the port the app runs on
EXPOSE 80

# Command to run the app
CMD ["gunicorn", "--workers=6", "--bind=0.0.0.0:80", "--timeout=180", "app:app"]
