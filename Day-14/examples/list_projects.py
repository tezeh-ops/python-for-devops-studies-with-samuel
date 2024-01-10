# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://samuel-munoh.atlassian.net/rest/api/3/project"

API_TOKEN = "ATATT3xFfGF0R9hJa4wYjvyH6haHpr1dWcv8w1_gtRQctAMtsy-SdcSIG-_MXrO-TUGIrEe3FVzuB-TOO-3ZKvCS5AIq9cLOHMaWk8x69tJunAPHaw0fAyztrHnpT3tlLk6zzZeRxJSBXM0q6gEyV-27P-KOR1Sqgq3fGjkNg7LjRD_uMTv6HVY=DA0328D4"

auth = HTTPBasicAuth("samuelmunoh@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

name = output[0]["name"]

print(name)