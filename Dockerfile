# Use the official PyTorch base image
FROM python:3.9-slim

# Set the working directory inside the container

RUN mkdir /digitalisim

WORKDIR /digitalisim

# Copy the requirements file
COPY requirements.txt /digitalisim/

# Install the Python dependencies
RUN pip install --no-cache-dir -r /digitalisim/requirements.txt

# Installer les dépendances nécessaires pour le client MySQL
RUN apt-get update && \
    apt-get install -y default-mysql-client && \
    rm -rf /var/lib/apt/lists/*

# Copy the application code to the container
COPY /app /digitalisim/app
COPY wait-for-it.sh /digitalisim/

# Expose the app's port

ENV PYTHONPATH "${PYTHONPATH}:/digitalisim"

EXPOSE 8000

# Start the FastAPI server
CMD ["./wait-for-it.sh", "db:3306", "uvicorn", "app.main:app", "--host", "0.0.0.0","--port", "8000"]
