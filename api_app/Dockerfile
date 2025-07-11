# Use the Python 3.11.0 base image
FROM python:3.11.5

# Set the working directory inside the container
WORKDIR /code

# Copy the requirements.txt file to the container
COPY requirements.txt requirements.txt

# Install the Python dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the entire local directory to the container's working directory
COPY . .

# Expose port for the container
EXPOSE ${CONTAINER_PORT}

# Set the default command to run when the container starts
CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", ${CONTAINER_PORT}]
