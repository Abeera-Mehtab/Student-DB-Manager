# Use an official Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy only required files
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the code
COPY . .

# Set env var to prevent Python from buffering outputs
ENV PYTHONUNBUFFERED=1

# Run the app
CMD ["python", "app.py"]

