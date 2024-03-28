#### Import Enrollments from Json Payload ####

import requests
import json
import base64

# Endpoint and credentials
url = 'https://fhir.demo.hispsrilanka.org/dhis/api/enrollments'
username = 'dcadmin'
password = 'Admin@Dhar123'

# Read the JSON file
with open('NewEnrollments.json', 'r') as file:
    data = json.load(file)

# Split the data into chunks (e.g., size 100)
chunk_size = 150
chunks = [data['enrollments'][i:i + chunk_size] for i in range(0, len(data['enrollments']), chunk_size)]

# Iterate over chunks and send requests
for chunk in chunks:
    # Encode username and password for basic authentication
    auth = base64.b64encode(bytes(f'{username}:{password}', 'utf-8')).decode('utf-8')
    
    # Create headers with authentication
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic ' + auth
    }
    
    # Send POST request
    response = requests.post(url, headers=headers, json={'enrollments': chunk})
    
    # Check response status
    if response.status_code == 200:
        print(f"Successfully inserted {len(chunk)} enrollments")
    else:
        print(f"Failed to insert enrollments. Status code: {response.status_code}, Response: {response.text}")
