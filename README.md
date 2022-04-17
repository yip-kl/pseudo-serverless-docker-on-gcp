# Execute Notebook with Docker
Build Docker image to execute Notebook on-demand

<b>Test running the container locally</b>
1. Add the requirements by executing ```pip3 freeze > requirements.txt``` when the virtual environment activated
2. Build with ```docker build -t image_name .```
3. Run with ```docker run -it image_name notebook_execution.py```

<b>Deploy the container to Compute Engine</b>
1. Submit container image to GCP, see <a href="https://cloud.google.com/build/docs/building/build-containers#use-dockerfile">here</a>
2. Create instance and deploy container according to the instruction <a href="https://cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance">here</a>

Note: Remember to perform these actions too
- Remove the service account anthentication from the script, and set the right identity for the VM 
- Make container's Restart Policy "On Failure" instead of "Always", otherwise the container could be up for less than 10 seconds for commands with short execution time and thus keep starting, see <a href="https://docs.docker.com/config/containers/start-containers-automatically/">here</a>
- If you are going to deploy it as Cloud Function, include items listed in the requirements.txt
