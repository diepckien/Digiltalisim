# Use the official PyTorch base image
FROM python:3.9-slim

# Create a non-root user and group
RUN groupadd -r appgroup && useradd -r -g appgroup -m appuser

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

# Set permissions to allow the non-root user to access the working directory
RUN chown -R appuser:appgroup /digitalisim

# Set environment variables
ENV PYTHONPATH "${PYTHONPATH}:/digitalisim"

# Expose the app's port
EXPOSE 8000

# Switch to the non-root user
USER appuser

# Start the FastAPI server
CMD ["./wait-for-it.sh", "db:3306", "uvicorn", "app.main:app", "--host", "0.0.0.0","--port", "8000"]
