
# here we want to make an API call to Jira Dashboard to list all the project we have on the dashboard.

# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests                      # making api with request
from requests.auth import HTTPBasicAuth     # importing this package and we want to make use of the module < HTTPBasicAuth >
import json

#url = "https://your-domain.atlassian.net/rest/api/3/project"    # we will change this URL to the URL of our Jira dashboard = < https://samuel-munoh.atlassian.net/ >

url = "https://samuel-munoh.atlassian.net/rest/api/3/project"

#auth = HTTPBasicAuth("email@example.com", "<api_token>")  Providing your email and token see below ( NB for best practice we could call the API Token as ENV)

API_TOKEN="ATATT3xFfGF08jImXsAl2VSXwrbyVRB6j7LLQK8_HfZGx3l_mUabms9E4FlxUBBh-ae9mKC7fgYOAapk0F6qqEtlyE97PnkyKSdpIrP0gcZcVwIO1hnbUGqV_9j8JqFlfdAJPyBHrgAyTz4IipZ0319fQrRxxW3o7o48HGnGxd3dMfjwWLXFIgM=68DE5DA3"

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

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


# =====================================We could just end it above but since we want tyo handel the JSON format to have the name of the the Project by usin Indexing we continue below===


output = json.loads(response.text)

name = output[0]["name"]

print(name)