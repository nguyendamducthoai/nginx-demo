# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY app.py .

# Expose port 8080 for the Flask app
EXPOSE 80

# Run the Flask application
CMD ["python", "app.py"]