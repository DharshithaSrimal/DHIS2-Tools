#### Import Enrollments from Json Payload ####

import requests
import json
import base64

# Endpoint and credentials
url = 'https://172.31.32.231/dhis/api/enrollments'
username = 'dharshitha'
password = 'Admin@Dhar123'

# Read the JSON file
with open('set4/NewEnrollments (1).json', 'r') as file:
    data = json.load(file)

# Split the data into chunks (e.g., size 100)
chunk_size = 1
chunks = [data['enrollments'][i:i + chunk_size] for i in range(0, len(data['enrollments']), chunk_size)]
failed_ids = []  # List to store failed trackedEntityIds

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
    response = requests.post(url + '?upsert=true', headers=headers, json={'enrollments': chunk}, verify=False)
    
    # Check response status
    if response.status_code == 201:
        print(f"Successfully inserted {len(chunk)} enrollments")
    else:
        # Log the failed enrollments to the file
        for tei in chunk:
            failed_ids.append(tei['trackedEntityInstance'])
        print(f"Failed to insert enrollments. Status code: {response.status_code}, Response: {response.text}")

# Write failed trackedEntityIds to a file
with open('failedEnrollments4.txt', 'w') as file:
    for failed_id in failed_ids:
        file.write(failed_id + '\n')

print("Failed enrollments written to failedEnrollments4.txt")