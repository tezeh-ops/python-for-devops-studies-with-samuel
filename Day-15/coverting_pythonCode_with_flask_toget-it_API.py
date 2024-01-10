

import requests
from requests.auth import HTTPBasicAuth
import json

from flask import Flask

app = Flask(__name__)

# Define a route that handles GET requests
@app.route('/createjira', methods=['POST'])
def createJira():

    url = "https://samuel-munoh.atlassian.net/rest/api/3/issue"

    API_TOKEN=" "  # paste your TOKEN here

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
                            "text": "Order entry fails when selecting supplier.",
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
           "key": "TRAC"
        },
        "issuetype": {
            "id": "10011"
        },
        "summary": "Main order flow broken",
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

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)