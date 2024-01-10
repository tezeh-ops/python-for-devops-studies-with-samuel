
# Here we want to create JIRA Ticket

# https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-post


# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://samuel-munoh.atlassian.net/rest/api/3/issue"

#auth = HTTPBasicAuth("email@example.com", "<api_token>")  Providing your email and token see below ( NB for best practice we could call the API Token as ENV)

API_TOKEN = "ATATT3xFfGF0R9hJa4wYjvyH6haHpr1dWcv8w1_gtRQctAMtsy-SdcSIG-_MXrO-TUGIrEe3FVzuB-TOO-3ZKvCS5AIq9cLOHMaWk8x69tJunAPHaw0fAyztrHnpT3tlLk6zzZeRxJSBXM0q6gEyV-27P-KOR1Sqgq3fGjkNg7LjRD_uMTv6HVY=DA0328D4"

auth = HTTPBasicAuth("samuelmunoh@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
   
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first JIRA Ticket.",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    
    "issuetype": {
      "id":   "10011"       #"10010"      # See the Note on EverNote to see the step to get the ID
    },
   
    "project": {
      "key": "TRAC"    # TRAC is what is given by default when we create the project on the dashboard ( just a shot form given for the project nmae)
    },
   
   
    "summary": "First  Jira Ticket",   # writ the summary of the ticket
 
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))