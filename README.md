# Pseudo-serverless Docker run on GCP
Spin up GCE automatically for Docker run, and tear it down upon completion. This could be useful if you find Cloud Run too restrictive (e.g. run time / spec limitation, forced to create a HTTP endpoint, etc.), or if you find running Docker via Vertex AI custom training job too expensive

The example concerned is for running Jupyter notebook with papermill, and storing the output in Google Cloud Storage

<b>Test running the container locally</b>
1. Add the requirements by executing ```pip3 freeze > requirements.txt``` when the virtual environment is activated
2. Build with ```docker build -t image_name .```
3. Run with ```docker run -it image_name```

<b>Deploy the container to Compute Engine</b>
1. Submit container image to Container Registry, see <a href="https://cloud.google.com/container-registry/docs/pushing-and-pulling">here</a>
2. Deploy Cloud Function to spin up the VM (refer to the ```cloud_function/spin_up``` folder for codes)
3. Deploy Cloud Function that tears down VM upon job finish, which is signaled by the log that is defined in ```notebook_execution.py``` (refer to the ```cloud_function/tear_down``` folder for codes)

<b>Troubleshooting</b>
- ```Kernel died while waiting for execute reply```: Try spin up a more powerful VM

To-do:
- deploy.sh for the Cloud Functions, and automate logging sink creation
