import requests
import json

# Set baseline unique Firestore instance connection details
# For Python / RestAPI project id and Firebase JWT tokens are mandatory
# jwt_token - firebase authentication token; if custom authentication is used, then custom JWT should be exchanged to Firebase token (POST to https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyCustomToken?key=PROJECT_jwt_token {"token":"CUSTOM_TOKEN","returnSecureToken":true}) which require also the api key of the Firestore project

jwt_token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjY5NjI5NzU5NmJiNWQ4N2NjOTc2Y2E2YmY0Mzc3NGE3YWE5OTMxMjkiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vc2VjbGFiLWVjNGE2IiwiYXVkIjoic2VjbGFiLWVjNGE2IiwiYXV0aF90aW1lIjoxNzA2NDIyODYxLCJ1c2VyX2lkIjoiVlNFck9vUXluMFYxTEtYWWJJa1RQbFN4WTgzMyIsInN1YiI6IlZTRXJPb1F5bjBWMUxLWFliSWtUUGxTeFk4MzMiLCJpYXQiOjE3MDY3NjUwNzgsImV4cCI6MTcwNjc2ODY3OCwiZW1haWwiOiJwZWRyYW0ubWVza291YmhhZ2hpZ2hpQG1haWwudXRvcm9udG8uY2EiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJwZWRyYW0ubWVza291YmhhZ2hpZ2hpQG1haWwudXRvcm9udG8uY2EiXX0sInNpZ25faW5fcHJvdmlkZXIiOiJwYXNzd29yZCJ9fQ.L4n-McpDtIZjTTiNye21HO55nyZg0fu2N49SdA3ukQR_l2pzB4pcT6Kq1QwCs16q7gd0YuK7EzfzAzkVi_AMnKCkabxkXFhz1kGwmBNQE6Ah-dBWxc6FuTDA0hN6WdHMdVXt_bza6KVYWtOh-KzCW_axqElR2f_CxW1jc1sVH3QekeDa0pGfvy-h42U8N88cVciUbEWus89PQ_dLOYUNbi9-22AaEYrRcw0PZxRWWha9PpPFYB7BrJxoVYdDLmqnK2Fc8ni06dvm1kxwpZ4ajImzhDJUHAqguN9HHuA0gVZqP7qRGin90jhDYInPzbqXHKiDAhA6s0qTeBO2Yp1Kxw-Token"
project_id = "seclab-ec4a6"

# Set the headers
headers = {"Authorization": f"Bearer {jwt_token}", "Content-Type": "application/json"}

collection_id = "CSCD27W24"
document_id = "your-document-id"
# This example sends a GET request to the Firestore REST API to read a document with the specified ID in the default database of your Firebase project. The response is a JSON object that contains the fields of the document.
# Send the request
base_url = f"https://firestore.googleapis.com/v1/projects/{project_id}/databases/(default)/documents/{document_id}"
response = requests.get(base_url, headers=headers)

# Get the document data
document = response.json()
data = document["fields"]
print(data)

# Here is an example of how to use the Firestore REST API in Python to write a document
# This example sends a PATCH request to the Firestore REST API to update a document with the specified ID in a collection with the specified ID in the default database of your Firebase project. The request includes the fields of the document in the request body as a JSON object.

base_url = f"https://firestore.googleapis.com/v1/projects/{project_id}/databases/(default)/documents/{collection_id}/{document_id}"

# Set the document data
data = {"fields": {"name": {"stringValue": "John Smith"}, "age": {"integerValue": 30}}}

# Send the request
response = requests.patch(base_url, json=data, headers=headers)

# Check the response status
if response.status_code == 200:
    print("Document updated successfully.")
else:
    print("Error updating document.")