import papermill as pm
from google.cloud import logging
import requests
import arrow

"""Define parameters"""

local_time = arrow.utcnow().to('+08:00')
today = local_time.format('YYYYMMDD')
timestamp = round(local_time.timestamp())

job_name = 'test_papermill'
notebook_name = 'current_time'
bucket_path = 'papermill_test'
kernel_name = 'python3'

input_path = f'{notebook_name}.ipynb'
output_path = f'gs://{bucket_path}/{notebook_name}-{today}-{timestamp}.ipynb'

"""Instantiates a logging client"""

# Instantiates a logging client
logging_client = logging.Client()

# Retrieves a Cloud Logging handler based on the environment
# you're running in and integrates the handler with the
# Python logging module. By default this captures all logs
# at INFO level and higher
logging_client.get_default_handler()
logging_client.setup_logging()
logger = logging_client.logger(job_name)

"""Execute the notebook"""

try:
    metadata_server = "http://metadata/computeMetadata/v1/instance/"
    metadata_flavor = {'Metadata-Flavor' : 'Google'}
    gce_hostname = requests.get(metadata_server + 'hostname', headers = metadata_flavor).text
except Exception as e:
    print(str(e))
    gce_hostname = ''

try:
  pm.execute_notebook(input_path,output_path,kernel_name=kernel_name)
  logger.log_struct(
    {"job_name": job_name, "execution_status": "success", "instance_hostname": gce_hostname, "message":""},
    severity='INFO')
except Exception as e:
  logger.log_struct(
    {"job_name": job_name, "execution_status": "failure", "instance_hostname": gce_hostname, "message":str(e)},
    severity='ERROR')
