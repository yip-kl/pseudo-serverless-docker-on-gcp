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
RUN pip install jupyter papermill gcsfs arrow google-cloud-logging
RUN pip install -r requirements.txt
RUN python -m ipykernel install --user --name=python3

# Copy code to working directory
WORKDIR /usr/src/app
COPY . .

# Execute the below upon run
ENTRYPOINT ["python3"]
CMD ["notebook_execution.py"]
