import requests
from requests.auth import HTTPBasicAuth

url_search_base = "https://dhis.dc.hispsrilanka.org/dhis/api/39/tracker/trackedEntities"
url_update_template = "https://dhis.dc.hispsrilanka.org/dhis/api/events/"
url_update = "https://dhis.dc.hispsrilanka.org/dhis/api/events?program=jwn5nGdUepW&programStage=Qpuicl4a94s&trackedEntityInstance="


attribute_id = "j92f54nkFoH"
attribute_values = [
           "3ec79086-c490-4479-95e8-da9f72967c45", "3ec79086-c490-4479-95e8-da9f72967c45", "3ec79086-c490-4479-95e8-da9f72967c45", "3ec79086-c490-4479-95e8-da9f72967c45", "3ec79086-c490-4479-95e8-da9f72967c45", "3ec79086-c490-4479-95e8-da9f72967c45", "3ec79086-c490-4479-95e8-da9f72967c45", "54d138ac-3df8-459c-ba40-bb7429713c42", "54d138ac-3df8-459c-ba40-bb7429713c42", "54d138ac-3df8-459c-ba40-bb7429713c42", "54d138ac-3df8-459c-ba40-bb7429713c42", "54d138ac-3df8-459c-ba40-bb7429713c42", "54d138ac-3df8-459c-ba40-bb7429713c42", "6d373f78-dcec-48f5-a309-cfc7677f14d0", "6d373f78-dcec-48f5-a309-cfc7677f14d0", "6d373f78-dcec-48f5-a309-cfc7677f14d0", "6d373f78-dcec-48f5-a309-cfc7677f14d0", "6d373f78-dcec-48f5-a309-cfc7677f14d0", "6d373f78-dcec-48f5-a309-cfc7677f14d0", "6d373f78-dcec-48f5-a309-cfc7677f14d0", "6d373f78-dcec-48f5-a309-cfc7677f14d0", "6d373f78-dcec-48f5-a309-cfc7677f14d0", "6d373f78-dcec-48f5-a309-cfc7677f14d0", "7dae0dd6-16a8-4c09-b3d7-09d761edf4f6", "799db2b6-59d9-46f7-9e30-313865628c45", "799db2b6-59d9-46f7-9e30-313865628c45", "799db2b6-59d9-46f7-9e30-313865628c45", "799db2b6-59d9-46f7-9e30-313865628c45", "799db2b6-59d9-46f7-9e30-313865628c45", "799db2b6-59d9-46f7-9e30-313865628c45", "1f0ae3bc-6fe9-4526-977e-e0ab4a260101", "1f0ae3bc-6fe9-4526-977e-e0ab4a260101", "1f0ae3bc-6fe9-4526-977e-e0ab4a260101", "1f0ae3bc-6fe9-4526-977e-e0ab4a260101", "1f0ae3bc-6fe9-4526-977e-e0ab4a260101", "1f0ae3bc-6fe9-4526-977e-e0ab4a260101", "1f0ae3bc-6fe9-4526-977e-e0ab4a260101", "1f0ae3bc-6fe9-4526-977e-e0ab4a260101", "1f0ae3bc-6fe9-4526-977e-e0ab4a260101", "1f0ae3bc-6fe9-4526-977e-e0ab4a260101", "1f0ae3bc-6fe9-4526-977e-e0ab4a260101", "1f0ae3bc-6fe9-4526-977e-e0ab4a260101", "1f0ae3bc-6fe9-4526-977e-e0ab4a260101", "1f0ae3bc-6fe9-4526-977e-e0ab4a260101", "1f0ae3bc-6fe9-4526-977e-e0ab4a260101", "1f0ae3bc-6fe9-4526-977e-e0ab4a260101", "1f0ae3bc-6fe9-4526-977e-e0ab4a260101", "2fc711b7-26d1-43f5-9dd4-de4457bb4771", "2fc711b7-26d1-43f5-9dd4-de4457bb4771", "4a2d8425-18ef-4b68-95bb-4a2d975102b1", "4a2d8425-18ef-4b68-95bb-4a2d975102b1", "6c49a564-4856-4c7e-97ab-6fdc1f0e32fa", "6c49a564-4856-4c7e-97ab-6fdc1f0e32fa", "cfa53e82-2324-4a92-951c-ef4091d385ba", "cfa53e82-2324-4a92-951c-ef4091d385ba", "cfa53e82-2324-4a92-951c-ef4091d385ba", "cfa53e82-2324-4a92-951c-ef4091d385ba", "cfa53e82-2324-4a92-951c-ef4091d385ba", "cfa53e82-2324-4a92-951c-ef4091d385ba", "886d38ea-3f61-4268-9c77-f9c4644260d7", "886d38ea-3f61-4268-9c77-f9c4644260d7", "886d38ea-3f61-4268-9c77-f9c4644260d7", "ce67dee1-ed76-44db-98c8-9d380bbeab1d", "ce67dee1-ed76-44db-98c8-9d380bbeab1d", "ce67dee1-ed76-44db-98c8-9d380bbeab1d", "ce67dee1-ed76-44db-98c8-9d380bbeab1d", "f0b3195d-64b9-4b25-b5cb-b7daec77ab10", "f0b3195d-64b9-4b25-b5cb-b7daec77ab10", "f0b3195d-64b9-4b25-b5cb-b7daec77ab10", "f0b3195d-64b9-4b25-b5cb-b7daec77ab10", "5eee31ea-3396-4a30-9905-4d3f295ede34", "e8945396-375e-4c9f-915c-c10c3dfef051", "e8945396-375e-4c9f-915c-c10c3dfef051", "ba5eec60-dcf1-46fb-b78a-86324bedee7f", "ba5eec60-dcf1-46fb-b78a-86324bedee7f", "44fa656d-d2a1-43f0-97d7-83a9591e3b65", "44fa656d-d2a1-43f0-97d7-83a9591e3b65", "44fa656d-d2a1-43f0-97d7-83a9591e3b65", "44fa656d-d2a1-43f0-97d7-83a9591e3b65", "44fa656d-d2a1-43f0-97d7-83a9591e3b65", "44fa656d-d2a1-43f0-97d7-83a9591e3b65", "44fa656d-d2a1-43f0-97d7-83a9591e3b65", "365e12f8-fee3-422f-9cde-572b8bb00d5d", "365e12f8-fee3-422f-9cde-572b8bb00d5d", "338e4e19-4827-478c-8941-89ece8308946", "338e4e19-4827-478c-8941-89ece8308946", "338e4e19-4827-478c-8941-89ece8308946", "338e4e19-4827-478c-8941-89ece8308946", "338e4e19-4827-478c-8941-89ece8308946", "338e4e19-4827-478c-8941-89ece8308946", "f728941e-1b7f-4922-b053-e04b6175e5e0", "f728941e-1b7f-4922-b053-e04b6175e5e0", "f728941e-1b7f-4922-b053-e04b6175e5e0", "f728941e-1b7f-4922-b053-e04b6175e5e0", "f728941e-1b7f-4922-b053-e04b6175e5e0", "f728941e-1b7f-4922-b053-e04b6175e5e0", "f728941e-1b7f-4922-b053-e04b6175e5e0", "f728941e-1b7f-4922-b053-e04b6175e5e0", "f728941e-1b7f-4922-b053-e04b6175e5e0", "b1a381a9-66be-46a5-b32f-de894c638db2", "3a19b053-0f7a-4e59-af10-81b536f18984", "3a19b053-0f7a-4e59-af10-81b536f18984", "3a19b053-0f7a-4e59-af10-81b536f18984", "3a19b053-0f7a-4e59-af10-81b536f18984", "3a19b053-0f7a-4e59-af10-81b536f18984", "3a19b053-0f7a-4e59-af10-81b536f18984", "3a19b053-0f7a-4e59-af10-81b536f18984", "3a19b053-0f7a-4e59-af10-81b536f18984", "3a19b053-0f7a-4e59-af10-81b536f18984", "3a19b053-0f7a-4e59-af10-81b536f18984", "3a19b053-0f7a-4e59-af10-81b536f18984", "88c92b96-8f21-4a0c-9a90-25345e77625b", "88c92b96-8f21-4a0c-9a90-25345e77625b", "88c92b96-8f21-4a0c-9a90-25345e77625b", "88c92b96-8f21-4a0c-9a90-25345e77625b"
]
program_id = "jwn5nGdUepW"
username = "dcadmin"
password = "Admin@Dhar123"
count = 0
for attribute_value in attribute_values:
    print(attribute_value)
    # Search for tracked entities with the specified attribute value
    search_params = {
        "program": program_id,
        "filter": f"{attribute_id}:eq:{attribute_value}",
        "ouMode": "ACCESSIBLE"
    }
    url_search = f"{url_search_base}?{'&'.join([f'{k}={v}' for k, v in search_params.items()])}"
    # print(f"Searching using URL: {url_search}")
    response = requests.get(url_search, auth=HTTPBasicAuth(username, password))
    if response.status_code == 200:
        response_json = response.json()
        if "instances" in response_json:
            count = count + 1
            print(count)
            instances = response_json["instances"]
            for instance in instances:
                tei_id = instance["trackedEntity"]
                url_updates = url_update + tei_id
                event_response = requests.get(url_updates, auth=HTTPBasicAuth(username, password))
                event_response_json = event_response.json()
                # print(event_response_json)
                events = event_response_json['events']
                for event in events:
                    dataValues = event['dataValues']
                    dead = {"dataElement": "nrTS05LkiaS", "value": "Dead"}
                    # dataValues_json = dataValues.json()
                    dataValues.append(dead)
                    event['dataValues'] = dataValues 
                    event_id = event['event']
                    print(url_update_template + event_id)
                    # print(event)
                    response_event = requests.post(url_update_template.format(event_id), auth=HTTPBasicAuth(username, password), json=event)
                    print(response_event.status_code)
               
        else:
            print(f"No instances found for attribute value {attribute_value}")
    else:
        print(f"Failed to search for tracked entities with attribute value {attribute_value}. Status code: {response.status_code}")