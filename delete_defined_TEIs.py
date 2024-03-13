import requests
from requests.auth import HTTPBasicAuth

url_template = "endpoint_url"
# Replace the TEIs
tracked_entity_instance_ids = [
    "ZiJk32XIWJH","pnIaw9YzHb9","uTn5fi47qOY","G6lM6YvcJM2","y2Iajvm8Ir2","RCXO8StXB1F","cY0r64gKD3B","dwj0AbV75F1","JKUTCqBOvBH","KZkrmZo56NE","ZvVafB4BtZK","zDapYkKeUlF","kP7HZ3Cxco5","Xo30PBmosFY","bnnhyaQH2b4","lHEXa1FKuWN","LAtYeWNFMve","naVftyTsQir","MGmL3VzjRrn","IoYAypQbeqN","yck0A2Rd0fC","U7onogaEYrB","kwhfM3mp7Aq","nhiXDkqII0S","Jxne8gAv9oK","Gi4PShJNfOY","sMu3ZEkkW4e"
]

username = "username"
password = "password"

for tei_id in tracked_entity_instance_ids:
    url = url_template + tei_id
    print(url)
    response = requests.delete(url, auth=HTTPBasicAuth(username, password))
    if response.status_code:
        print(f"{response.status_code} Tracked entity instance {tei_id} deleted successfully")
    else:
        print(f"{response.status_code} Failed to delete tracked entity instance {tei_id}. Status code: {response.status_code}")
