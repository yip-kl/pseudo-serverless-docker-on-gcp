# Execute Notebook with Docker
Build Docker image to execute Notebook on-demand

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
