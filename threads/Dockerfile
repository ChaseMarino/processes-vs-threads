# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

RUN pip install flask
# Copy the rest of the application code into the container
COPY . .

# Expose port 5000 for the Flask web server
EXPOSE 8080

# Start the web server when the container launches
CMD ["python", "threads.py"]
