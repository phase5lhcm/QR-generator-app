# Use Python base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install qrcode[pil]

# Run the QR generator
CMD ["python", "main.py"]
