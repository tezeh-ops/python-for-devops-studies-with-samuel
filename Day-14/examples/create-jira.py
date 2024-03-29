# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url =  "https://samuel-munoh.atlassian.net/rest/api/3/issue"

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
              "text": "My first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "project": {
      "key": "AB"
    },
    "issuetype": {
      "id": "10006"
    },
    "summary": "First JIRA Ticket",
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