# DHIS2 Tools

## Importing Data to DHIS2
1. Replace your endpoints and credentials in the importing scripts.
2. Use a JSON payload and replace the name of the JSON file with "NewTrackedEntityInstances.json".

### Import TEIs
Run `importTEI.py` script to import the TEIs.

### Import Enrollments
Run `importEnrollments.py` script to import the Enrollments.

### Import Events
Run `importEvents.py` script to import the Events.

## Removing Data from DHIS2

### Delete All TEIs 
Run `delete_all_TEIs.py` to soft delete all the TEIs from your DHIS2 instance.

### Delete Defined TEIs
First, define the TEIs in the array and then run `delete_defined_TEIs.py` to soft delete them from your DHIS2 instance.


