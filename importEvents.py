import requests
import json
import base64

# Endpoint and credentials
url = 'https://172.31.32.231/dhis/api/events'
username = 'dharshitha'
password = 'Admin@Dhar123'

# Read the JSON file
with open('set4/NewEvents (1).json', 'r') as file:
    data = json.load(file)

# Split the data into chunks (e.g., size 100)
chunk_size = 1
chunks = [data['events'][i:i + chunk_size] for i in range(0, len(data['events']), chunk_size)]

# Open a text file for writing failed events
with open('failedEvents4.txt', 'w') as failed_file:
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
        response = requests.post(url + '?upsert=true', headers=headers, json={'events': chunk}, verify=False)
        
        # Check response status
        if response.status_code == 200:
            print(f"Successfully inserted {len(chunk)} events")
        else:
            try:
                response_json = response.json()
                if 'importSummaries' in response_json:
                    for summary in response_json['importSummaries']:
                        if summary['status'] == 'ERROR':
                            conflicts = summary['conflicts']
                            if conflicts:
                                for conflict in conflicts:
                                    failed_file.write(f"Conflict: {conflict['value']}\n")
                        else:
                            failed_file.write(f"Import Summary: {summary['status']}\n")
            except json.JSONDecodeError:
                failed_file.write(f"Failed to insert events. Status code: {response.status_code}, Response: {response.text}\n")
