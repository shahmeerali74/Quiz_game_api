# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables for Python buffering and ensure Python output is sent straight to terminal without buffering it first
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory inside the container
WORKDIR /code

# Copy the dependencies file to the working directory
COPY requirements.txt /code/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . /code/

# Expose port 8000 to allow communication to/from server
EXPOSE 8081

# Command to run the Django API server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
