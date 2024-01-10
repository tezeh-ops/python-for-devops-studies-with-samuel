
import requests
from requests.auth import HTTPBasicAuth
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/createjira', methods=['POST'])
def create_jira():
    url = "https://samuel-munoh.atlassian.net/rest/api/3/issue"

    api_token = "your_jira_api_token"  # Replace with your actual Jira API token
    auth = HTTPBasicAuth("samuelmunoh@gmail.com", api_token)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    try:
        payload = request.get_json()
        comment = payload.get("comment", {}).get("body", "").lower()

        # Check if the comment contains "/jira" before creating a Jira ticket
        if "/jira" in comment:
            jira_payload = {
                "fields": {
                    "description": {
                        "content": [
                            {
                                "content": [
                                    {
                                        "text": comment,
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
                    "summary": "Jira issue created from comment",
                },
                "update": {}
            }

            response = requests.post(url, json=jira_payload, headers=headers, auth=auth)

            if response.status_code == 201:
                return jsonify(response.json()), 201
            else:
                return jsonify({"error": f"Failed to create Jira issue: {response.text}"}), 500
        else:
            return jsonify({"message": "No Jira issue created. Comment does not contain '/jira'."}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


#===============================================================================

# Here Below is just another update show how we can overide the summary message in our code and use the info writed by the issue creator on GitHub ==


import requests
from requests.auth import HTTPBasicAuth
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/createjira', methods=['POST'])
def create_jira():
    url = "https://samuel-munoh.atlassian.net/rest/api/3/issue"
    api_token = "your_jira_api_token"  # Replace with your actual Jira API token
    auth = HTTPBasicAuth("samuelmunoh@gmail.com", api_token)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    try:
        payload = request.get_json()

        # Extract the comment and check if it contains "/jira"
        comment = payload.get("comment", {}).get("body", "").lower()

        if "/jira" in comment:
            # Extract information from GitHub payload to customize the Jira issue
            github_user = payload.get("sender", {}).get("login", "")
            github_repo = payload.get("repository", {}).get("full_name", "")
            github_issue_number = payload.get("issue", {}).get("number", "")
            github_issue_title = payload.get("issue", {}).get("title", "")

            # Customize the Jira issue summary
            jira_summary = f"{github_user}/{github_repo} - GitHub Issue #{github_issue_number}: {github_issue_title}"

            jira_payload = {
                "fields": {
                    "description": {
                        "content": [
                            {
                                "content": [
                                    {
                                        "text": comment,
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
                    "summary": jira_summary,
                },
                "update": {}
            }

            response = requests.post(url, json=jira_payload, headers=headers, auth=auth)

            if response.status_code == 201:
                return jsonify(response.json()), 201
            else:
                return jsonify({"error": f"Failed to create Jira issue: {response.text}"}), 500
        else:
            return jsonify({"message": "No Jira issue created. Comment does not contain '/jira'."}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

