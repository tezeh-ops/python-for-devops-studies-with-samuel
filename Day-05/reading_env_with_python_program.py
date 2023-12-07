# Here we will see how we can use ENV to saved sensitive info

# To see the list of ENV in you OS we run < env> But since im using Windows(powershell)  the command is < Get-ChildItem env: >

# Now let set/create an ENV locally and to that with powershell==<  $env:password = "samuel" >  and it will creat this password locally


# Next let see how we can call this password into our python program with hardCoding the passowrd in our code

# In python to do that we use a MODULE call < os >  so let impoet the module;




import os       


print(os.getenv("password"))      # here we want to print the password 



# And if we don't to print it wecan jus say

#password = os.getenv("password")



#====================================================>
# when run this the result we got 

#PS C:\Users\Samue\python-for-devops\Day-05> python .\reading_env_with_python_program.py 
           
#   samuel
#==========================================================>