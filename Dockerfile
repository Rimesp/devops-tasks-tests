# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application files to the container
COPY . /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run the tests when the container is built (optional, for debugging)
RUN pytest --cov=devops_tasks --cov-report=xml || echo "Tests Failed"

# Default command to run the Python app (replace with actual run logic if needed)
CMD ["python", "devops_tasks.py"]
