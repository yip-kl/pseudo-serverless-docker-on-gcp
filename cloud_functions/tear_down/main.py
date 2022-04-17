import sys
import time
import base64
import json
from google.cloud import compute_v1

pubsub_string = base64.b64decode(event['data']).decode('utf-8')
pubsub_json = json.loads(pubsub_string)
gce_hostname_split = pubsub_json['gce_hostname'].split(".")

if len(gce_hostname_split) == 5:
    machine_name, zone, c, project_id, internal = gce_name_split
elif len(gce_hostname_split) == 4:
    machine_name, c, project_id, internal = gce_name_split
    
def delete_instance(event, context):
    """
    Send an instance deletion request to the Compute Engine API and wait for it to complete.

    Args:
        project_id: project ID or project number of the Cloud project you want to use.
        zone: name of the zone you want to use. For example: “us-west3-b”
        machine_name: name of the machine you want to delete.
    """
    
    instance_client = compute_v1.InstancesClient()
    operation_client = compute_v1.ZoneOperationsClient()

    print(f"Deleting {machine_name} from {zone}...")
    operation = instance_client.delete_unary(
        project=project_id, zone=zone, instance=machine_name
    )
    start = time.time()
    while operation.status != compute_v1.Operation.Status.DONE:
        operation = operation_client.wait(
            operation=operation.name, zone=zone, project=project_id
        )
        if time.time() - start >= 300:  # 5 minutes
            raise TimeoutError()
    if operation.error:
        print("Error during deletion:", operation.error, file=sys.stderr)
        return
    if operation.warnings:
        print("Warning during deletion:", operation.warnings, file=sys.stderr)
    print(f"Instance {machine_name} deleted.")
    return
