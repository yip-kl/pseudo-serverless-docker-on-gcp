# Run Docker in a pseudo-serverless manner
Spin up / tear down GCE automatically for Docker run. This could be useful if you find Cloud Run too restrictive (e.g. run time / spec limitation, forced to create a HTTP endpoint, etc.)

<b>Test running the container locally</b>
1. Add the requirements by executing ```pip3 freeze > requirements.txt``` when the virtual environment activated
2. Build with ```docker build -t image_name .```
3. Run with ```docker run -it image_name```

<b>Deploy the container to Compute Engine</b>
1. Submit container image to GCP, see <a href="https://cloud.google.com/build/docs/building/build-containers#use-dockerfile">here</a>
2. Deploy Cloud Function to spin up the VM (refer to the ```cloud_function/spin_up``` folder for codes)
3. Deploy Cloud Function that tears down VM upon job finish, which is signaled by the log that is defined in ```notebook_execution.py``` (refer to the ```cloud_function/tear_down``` folder for codes)

To-do:
- deploy.sh for the Cloud Functions, and automate logging sink creation
