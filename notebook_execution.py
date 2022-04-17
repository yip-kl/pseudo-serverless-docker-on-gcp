import papermill as pm
from google.cloud import logging
import datetime 
import time
import pytz

"""Define parameters"""

today = datetime.datetime.now(pytz.timezone('Asia/Hong_Kong')).strftime('%Y%m%d')
timestamp = round(time.time())

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
  pm.execute_notebook(input_path,output_path,kernel_name=kernel_name)
  logger.log_struct(
    {"job_name": job_name, "execution_status": "success", "message":""},
    severity='INFO')
except Exception as e:
  logger.log_struct(
    {"job_name": job_name, "execution_status": "failure", "message":str(e)},
    severity='ERROR')
