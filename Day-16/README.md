Beginner & intermediate level python interview Q&A  for DevOps 

1.  Describe a real-world example of how you python to solve a DevOps challenge? I have work on different project to solve different issue, but the most recent project i did was issue that brought up to me with a problem statement  where we have our source code  code that is maintain in GitHub  Repo and  and we have JIRA where we have to track all the work we do. So there was a requirement that was given to me by the development that  < when ever a developer comes to a Pull Request on GitHub due to the issue raise and if the issue need to be work on and developer  need to created a ticket for that issue on Jira instead of going to Jira all the time he can just confirms with a comment like ( /ticket   or / jira ) in the comment box and a python script should trigger and the python script should create a JIRA ticket will the info that is available on that pull request.   So how did i solve this problem:
> I wrote a python script covert it to a Flask base application to expose the Python script API so that GitHub can be able to talk to it. 
> With the python API expose i use GitHub Webhook to connect them together so that when the  developer comment </Jira > it will send all the information in a JSON format to python program and if the python program sees that there is a < /Jira > in the comment it will now create the Ticket in Jira by also talking to Jira API.

2. Discuss the challenges that you have face while using python for DevOps and how  you overcome it?  of cause  doing the project i explained above i did get it right the first time i face some issues with :
> Figuring out how to get the  < issue  type or task   ID >  so i had to explore the documentation and some other resources and finally got the way to git it which i did by going to the Jira board and navigated to the project and follow steps there to get it. 
> Since I'm not coming from a development background when i wrote the python it jus t script without it API expose and for me to expose the API i had to covert the python script into a Flask application and expose it and it was a little bit tricky but got it done 
> Another issue i face is that when i wrote the code i didn't pass in good condition that the ticket should only be create if the word < /jira > is use in the comment. since the  condition was not passed what ever was commented a Jira ticket will be created. so i had to fix that with conditions handling in the code.

3. How can you secure your python code and scripts? i will secure my code in this manner:
> make sure every sensitive info in handle as ENV
> i will make use of command line argument
> i will restrict access  to the OS because variables are being store in it. 

4. Explain  the difference between mutable and immutable objects?  In python, mutable ob jects can be altered after creation. WHILE  Immutable objects can't be changed once created. For instance Mutable object like list can be modified. While immutable object like  tuple cannot be altered.
5.  what is the difference between LIST and Tuple ?    NB <it same question as above but jus in a different way  >
6. Explain the use of Virtualenv?  Virtual-env create  isolated python environments, allowing different projects to use different versions of packages without conflict. 
7. What are Decorators in python ? decorators modify the behavior of function. They take a function as an argument, add some functionality, and return another function without modifying the original function,s code. 
8. How does exceptional handling work in python?  Exception handling in python uses < try, except, else, and finally blocks. > 

9. Explain the use of Lambda functions in python.? lambda functions are anonymous function used for short tasks.  For example:
>  Defining and using a lambda function;
```
square = lambda x: x**2
print(square(5))        # and output = 25
```

10. What are the different types of loops in python?
> for loop
```
for i in range(5):
    print(i)
```
> While loop
```
i = 0 
while i < 5:
    print(i)
    i += 1
```

11. Explain the different between  ==  and is  operators ? The == operators compare the values of two objects. While  the  is operators checks if two variables point to the same object in memory. 
12. What is the different between Global and Local Variables?  Global Var  are defined outside the function and can be accessed anywhere in the code. WHILE  Local var are defined inside function and only accessible within the function's scope . 
13. Explain the difference between open()  and with open()  statement?  open() is a built-in used to open a file andf return a file object. However, it's crucial to manually close the file using file_object.close(). Conversely,  with open() is a context manager that automatically handles file closure, ensuring clean-up even if exception ocure.
EXAMPLE:
.>   using  <  open() > 
```
# using < open >

file = open('example.txt', 'r')
content = file.read
file.close()            # if we don't close it manually here or at the end of the function thr file will remain open
```

> using < with open() >  which the best one to use
```
# Using < With Open >

with open('erxample.txt'  'r') as file:
    content = file.read()
 
# File ia automatically close when the block exits
```
