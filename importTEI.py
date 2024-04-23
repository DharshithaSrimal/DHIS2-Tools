#### Import TEIs from Json Payload ####

import requests
import json
import base64

# Endpoint and credentials
url = 'https://fhir.demo.hispsrilanka.org/dhis/api/trackedEntityInstances'
# url = 'http://localhost:8084/dhis/api/trackedEntityInstances'
# username = 'admin'
# password = 'district'
username = 'dcadmin'
password = 'Admin@Dhar123'

# Read the JSON file
with open('ds3/NewTrackedEntityInstances.json', 'r') as file:
    data = json.load(file)

# Split the data into chunks (e.g., size 50)
chunk_size = 10
chunks = [data['trackedEntityInstances'][i:i + chunk_size] for i in range(0, len(data['trackedEntityInstances']), chunk_size)]

# Iterate over chunks and send requests
for chunk in chunks:
    # Encode username and password for basic authentication
    auth = base64.b64encode(bytes(f'{username}:{password}', 'utf-8')).decode('utf-8')
    
    # Create headers with authentication
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic ' + auth
    }
    
    # Send POST request with upsert parameter
    response = requests.post(url + '?upsert=true', headers=headers, json={'trackedEntityInstances': chunk})
    
    # Check response status
    if response.status_code == 200:
        print(f"Successfully inserted or updated {len(chunk)} tracked entity instances")
    else:
        print(f"Failed to insert or update tracked entity instances. Status code: {response.status_code}, Response: {response.text}")
