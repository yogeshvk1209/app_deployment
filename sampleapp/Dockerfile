# Use a Python 3.9 base image for better compatibility
FROM python:3.9-slim

# Set maintainer label
LABEL maintainer="yogeshvk1209@gmail.com"

# Install sudo (optional, only if needed by the app)
RUN apt-get update && apt-get install -y sudo && apt-get clean && rm -rf /var/lib/apt/lists/*

# Add taskuser and set up home directory
RUN useradd -m taskuser && echo "taskuser:taskuser" | chpasswd

# Copy source files
COPY ./src/ /src/

# Install app dependencies
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r /src/requirements.txt

# Expose port
EXPOSE 8080

# Run as non-root user
USER taskuser

# Run the application
CMD ["python3", "/src/pytask.py", "--port", "8080"]
