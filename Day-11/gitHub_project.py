
# Project OUTLINE:

#1 Get PULL Request information on a Repo  using Python.
# E.g we will use Kubernetes Repo this demo  here since it a open source.

# STEPS WE WILL TAKE:
#> Use the <request module>

#  > Taking to the < GitHub API >

#3 > NB every info we get by tallking to the API always come in a JSON Formatt ( so we need to convert JSON to DICTIONARY) 

#4> Print the requirement

#===================================================== CODING BEGINS+++++++++++++++++++++>

import requests


# URL to fetch pull requests from the GitHub API
response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

'''
print(response)     # it will give us a result = < <Response [200]> >  But let get it in JSON 

'''
# This how we comment multiple lins in python
'''
print(response.json())   
'''
#   <print(reponse.json() ) this will give us a pig log of the information and when we use <.json > the file infrom will AUTOMATICLLY be coverted to a DICTIONARY

# and the above will give us every thing which too much of this that we don't need

# So Here we just want to print the Name of the person that created the PULL REQUEST:

complete_detalis = response.json()

print(complete_detalis[0]["id"])    #and this give  give us the id= 1652368798  which mean is working

# let see if we can get the name of the user:

print(complete_detalis[0]["user"]["login"])   # here is the name = < neolit123 >


# Now how can we get all the detail of all the userthat has created the Pull request :
# Here we will make use of < FOR  LOOP >  And it will print out all the name of those that has create a pull request

for element in range(len(complete_detalis) ): 

    print(complete_detalis[element]["user"]["login"]) 

# let add more flesh to to also print how many Pull request did they creat.



# ===  look at the complet code in this file call <04-demo-github-integration.py >