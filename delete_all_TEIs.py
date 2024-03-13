import requests

base_url = 'endpoint_url'
username = "username"
password = "password"

# Fetch organization units
org_units_url = base_url + 'organisationUnits.json'
response = requests.get(org_units_url, auth=(username, password))
org_units = response.json()['organisationUnits']

# Loop through each organization unit to delete tracked entity instances
for org_unit in org_units:
    org_unit_id = org_unit['id']
    delete_url = f"{base_url}/trackedEntityInstances.json?ou={org_unit_id}&program=jwn5nGdUepW"
    response = requests.get(delete_url, auth=(username, password))
    tracked_entity_instances = response.json()['trackedEntityInstances']
    
    # Delete each tracked entity instance
    for tei in tracked_entity_instances:
        tei_id = tei['trackedEntityInstance']
        delete_instance_url = f"{base_url}/trackedEntityInstances/{tei_id}"
        response = requests.delete(delete_instance_url, auth=(username, password))
        if response.status_code == 200:
            print(f"Deleted TEI {tei_id} for org unit {org_unit_id}")
        else:
            print(f"Failed to delete TEI {tei_id} for org unit {org_unit_id}: {response.text}")
