# Use an official Python runtime as a parent image
FROM python:3.13-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del .build-deps

# Copy the rest of the project files into the container at /app
COPY . /app/

# Expose the port (optional, depending on your project setup)
EXPOSE 8000

# Command to run Scrapy to start crawling
CMD ["scrapy", "crawl", "wwr"]
