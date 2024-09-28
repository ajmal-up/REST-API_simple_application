# Dockerfile
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt ./

# Install dependencies
RUN pip install -r requirements.txt

# Copy application code
COPY app.py ./

# Expose the port
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
