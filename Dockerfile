# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.9-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Copy application dependency manifests to the container image.
# Copying this separately prevents re-running pip install on every code change.
COPY requirements.txt ./

# Install production dependencies.
RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt

# Run Notebook
WORKDIR /usr/src/app
COPY . .
CMD ["notebook_execution.py"]
ENTRYPOINT ["python3"]
