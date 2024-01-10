# Github-JIRA intergration Project

the project outline:
The problem statement=
> There are a lot of QE or Devs engineers, when they notice a problem may be due to testing they will create an issue on the GitHub Repo. NB= let say not all issues  are issues so let say once every-week a developer will go to the GitHub Repo  to understand if the issues created are genius issues or not and if the issue is not valid  they have to close it and if the issue is valid then they have to work on it.  So Now for them to show the organization of the issue that need to be work as they have seen in GitHub, they have to  go the  JIRA dashboard and create Ticket on those various issues that need to be address. ( By doing so is going to be so much work on the develop team ) So the the developers comes to the DevOps engineers and ask if the y can Automate the ticker creating process with JIRA ?

Solution as DevOps Engineer:
Here we are going to automate these process in to  part:
1. GitHub   2)   JIRA       >>  and we are going to create a bridge between them so that when someone comment with e.g /jira in GitHub then the ticket will be automatically created in JIRA Dashboard.

- We will use python instead of Bash shell scripting  due to the dynamic nature  of the code that is need.  And we are going to write a program that when ever someone write a comment  on GitHub with ( /Jira) the GitHub will use the program and by doing so we will configure:
> A webhook  to connect  GitHub with our python code so that when someone Comment with ( /Jira) ok GitHub will see all the issue description of the issue ( like who created it, why,  what is needed  etc )  and all the comment on the GitHub related to it will be converted to JSON and send to our python program and this program is going to be running on an EC2 instance.  So when the info is converted in JSON format, from the program we will make:
> An API call to JIRA. 

HERE is what wee need:

1. Jira set up
   
2. understand Jira API calls [ there are two ways to talk to an application ( by  API or CLI ) and to use the API we need to set up the  < API Token >;   ApI Token is nothing but an authentication like Username  or password but for more security we go with Token because we can play with to with RBAC ( control the level of operation).  
Next let go to dashboard and created the API Token == 
- Go the our profile icon 
- select profile then click Manage account
- At the Top select security  then look down and  you will see  API TOKEN then click on < Create and manage API token >
- Click on Create APi < then enter a name for your token e.g python > the click create and copy the Token and saved it ( my token is = <ATATT3xFfGF0lwdwUVbGRsdQrmce3uv9isQpr6r97_186nCRf9-k_QET44KOuc63Cfs5ZbcoWgoPBKB1rMkCAWum6z4pXG_CsJh9YAexKF_4Bvv3klhEZr54Vtwgof4knUwr5F8ehFyOFGkkLz50WL4hH9gaOE2qEUEt4mR5WdMX4CLxs-AFIFU=F25387CF  > 
Next let understand Jira Rest API by going to the Doc = <  The Jira Cloud platform REST API (atlassian.com) >:
Example :
> let say using JIRA API we what to list all the Project we have in Jira dashboard with looking on the dashboard. [ And with the Jira Doc the API are very easy to use :
- on the API Doc above on the side look for Project
- Click on the Project  and at the right use will all the code available to use in different Languages (python, java, nodeJs   etc )..
- click on the Language you want to use ( for this demo is Python ) the copy the code and past in your IDE ==
below is the code we copied=
```
# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
url = "https://your-domain.atlassian.net/rest/api/3/project"
auth = HTTPBasicAuth("email@example.com", "<api_token>")
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
```


3. Write the python script==  < list_jira_project.py >
```
# here we want to make an API call to Jira Dashboard to list all the project we have on the dashboard.
# This code sample uses the 'requests' library:
# http://docs.python-requests.org

import requests
from requests.auth import HTTPBasicAuth
import json
#url = "https://your-domain.atlassian.net/rest/api/3/project"    # we will change this URL to the URL of our Jira dashboard = < https://samuel-munoh.atlassian.net/ >
url = "https://samuel-munoh.atlassian.net/rest/api/3/project"
#auth = HTTPBasicAuth("email@example.com", "<api_token>")  Providing your email and token see below ( NB for best practice we could call the API Token as ENV)

API_TOKEN="ATATT3xFfGF0R9hJa4wYjvyH6haHpr1dWcv8w1_gtRQctAMtsy-SdcSIG-_MXrO-TUGIrEe3FVzuB-TOO-3ZKvCS5AIq9cLOHMaWk8x69tJunAPHaw0fAyztrHnpT3tlLk6zzZeRxJSBXM0q6gEyV-27P-KOR1Sqgq3fGjkNg7LjRD_uMTv6HVY=DA0328D4"

auth = HTTPBasicAuth("samuelmunoh@gamil.com", API_TOKEN)
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
```

4)Execution of the script = <  python list_jira_project.py  > 

NB= If we have project on Jira dashboard it will list them in a JSON Format and if we don't understand it we can use any JSON formatter website to format the result in order to understand it.  Here is the JSON Formatter web link == < https://jsonformatter.org/ >  click on it and paste the JSON result and the click  <format/beautify> and it will restructured the JSON result and show the various project in sections and their names and more. ==


NOW TO SOLVE OUR PROBLE ABOVE :
> To Crete a Jira Ticket using  Python
> we will go back to the Jira Api Doc:


- serach for < issue> because jira Ticket are basically call < issue >
- then click on create issue and choose the language you want and copy the code APi>=
```
# Here we want to create JIRA Ticket
# https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-post
# This code sample uses the 'requests' library:
# http://docs.python-requests.org

import requests
from requests.auth import HTTPBasicAuth
import json
url = "https://your-domain.atlassian.net/rest/api/3/issue"
auth = HTTPBasicAuth("email@example.com", "<api_token>")
headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}
payload = json.dumps( {                # here jira is give us all the fills that can be use to create an issue/ticket and as we know not all are mandatory to use.
  "fields": {
    "assignee": {
      "id": "5b109f2e9729b51b54dc274d"
    },
    "components": [
      {
        "id": "10000"
      }
    ],
    "customfield_10000": "09/Jun/19",
    "customfield_20000": "06/Jul/19 3:25 PM",
    "customfield_30000": [
      "10000",
      "10002"
    ],
    "customfield_40000": {
      "content": [
        {
          "content": [
            {
              "text": "Occurs on all orders",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "customfield_50000": {
      "content": [
        {
          "content": [
            {
              "text": "Could impact day-to-day work.",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "customfield_60000": "jira-software-users",
    "customfield_70000": [
      "jira-administrators",
      "jira-software-users"
    ],
    "customfield_80000": {
      "value": "red"
    },
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
    "duedate": "2019-05-11",
    "environment": {
      "content": [
        {
          "content": [
            {
              "text": "UAT",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "fixVersions": [
      {
        "id": "10001"
      }
    ],
    "issuetype": {
      "id": "10000"
    },
    "labels": [
      "bugfix",
      "blitz_test"
    ],
    "parent": {
      "key": "PROJ-123"
    },
    "priority": {
      "id": "20000"
    },
    "project": {
      "id": "10000"
    },
    "reporter": {
      "id": "5b10a2844c20165700ede21g"
    },
    "security": {
      "id": "10000"
    },
    "summary": "Main order flow broken",
    "timetracking": {
      "originalEstimate": "10",
      "remainingEstimate": "5"
    },
    "versions": [
      {
        "id": "10000"
      }
    ]
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
```
NB= in our code we are only going to use the fills that are mandatory :
- Project name
- issue type 
- summary
- Reporter 
All this above are mandatory fills that we must have in out issue/ticket ( that is why before you are able to automat a task you must know how to create that task manually to know all the necessary fills. 
Next > we can go now in our code and remove the fills that are not actually needed.
NB = to get the
```
"issuetype": {
      "id": "10010"      # How to get the issue ID;
    },
```
> Go the Jira dashboard and click on project and select one the click the <...>
 next click < configure board >
>Click on < issue type>
> next  the click on < Story> ==
>
Next = look and the URL on the browser it will end withy a number copy that number it will be the issue ID e.g < ......ira/software/projects/TRAC/settings/issuetypes/10010 >
NB= same process for all if it Bug, Task, etc just click on it and copy the number at the end of the URL and use it .

Here below is the code to create our < Ticket/issue of a project using python with API Token > 

```
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
      "id":   "10010"      # See the Note on EverNote to see the step to get the ID
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
```

==========> Here we are running the code 
PS C:\Users\Samue\python-for-devops\Day-14> python .\Automate_creating-jira_ticket_with-python.py       < below is our result> ==
{
    "id": "10021",
    "key": "TRAC-3",
    "self": "https://samuel-munoh.atlassian.net/rest/api/3/issue/10021"
}
========> And now we can see that the Ticket was actually created on Jira ===


