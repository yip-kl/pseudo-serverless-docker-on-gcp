import googleapiclient.discovery
import requests

metadata_server = "http://metadata.google.internal/computeMetadata/v1/project/project-id"
metadata_flavor = {'Metadata-Flavor' : 'Google'}

project_id = requests.get(metadata_server, headers = metadata_flavor).text
instance_name = f'instance-{random.randint(0, 10000000)}'
region = "us-central1"
zone = "us-central1-a"
image_path = "gcr.io/adroit-hall-301111/exec_notebook"

config = {
  "canIpForward": False,
  "confidentialInstanceConfig": {
    "enableConfidentialCompute": False
  },
  "deletionProtection": False,
  "description": "",
  "disks": [
    {
      "autoDelete": True,
      "boot": True,
      "deviceName": f"{instance_name}",
      "initializeParams": {
        "diskSizeGb": "10",
        "diskType": f"projects/{project_id}/zones/{zone}/diskTypes/pd-balanced",
        "labels": {},
        "sourceImage": "projects/cos-cloud/global/images/cos-stable-97-16919-29-9"
      },
      "mode": "READ_WRITE",
      "type": "PERSISTENT"
    }
  ],
  "displayDevice": {
    "enableDisplay": False
  },
  "guestAccelerators": [],
  "labels": {
    "container-vm": "cos-stable-97-16919-29-9"
  },
  "machineType": f"projects/{project_id}/zones/{zone}/machineTypes/e2-medium",
  "metadata": {
    "items": [
      {
        "key": "gce-container-declaration",
        "value": f"spec:\n  containers:\n  - name: {instance_name}\n    image: {image_path}\n    stdin: False\n    tty: False\n  restartPolicy: Never\n# This container declaration format is not public API and may change without notice. Please\n# use gcloud command-line tool or Google Cloud Console to run Containers on Google Compute Engine."
      }
    ]
  },
  "name": instance_name,
  "networkInterfaces": [
    {
      "accessConfigs": [
        {
          "name": "External NAT",
          "networkTier": "PREMIUM"
        }
      ],
      "subnetwork": f"projects/{project_id}/regions/{region}/subnetworks/default"
    }
  ],
  "reservationAffinity": {
    "consumeReservationType": "ANY_RESERVATION"
  },
  "scheduling": {
    "automaticRestart": True,
    "onHostMaintenance": "MIGRATE",
    "preemptible": False
  },
  "serviceAccounts": [
    {
      "email": "712368347106-compute@developer.gserviceaccount.com",
      "scopes": [
        "https://www.googleapis.com/auth/cloud-platform",
      ]
    }
  ],
  "shieldedInstanceConfig": {
    "enableIntegrityMonitoring": True,
    "enableSecureBoot": False,
    "enableVtpm": True
  },
  "tags": {
    "items": []
  },
  "zone": f"projects/{project_id}/zones/{zone}"
}

def create_instance(event, context):
    compute = googleapiclient.discovery.build('compute', 'v1')
    compute.instances().insert(
        project=project_id,
        zone=zone,
        body=config).execute()
