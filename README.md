# Execute Notebook with Docker
Build Docker image to execute notebook (notebook_execution.py)

<b>Test running the container locally</b>
1. Build with ```docker build -t image_name```
2. Run with ```docker run -it image_name notebook_execution.py```

<b>Deploy the container to Compute Engine</b>
1. Create instance and deploy container according to the instruction <a href="https://cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance">here</a>
