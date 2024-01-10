# Here we will see how to write a flask program 

from flask import Flask   # here we are saying from the Flask module we have install in our system Import to ust the Flask ( why do we do it so? this because Flask is huge
                           # package and we don't bring out just the module we need it will take a long time for our application to run)

app = Flask(__name__)      # this a common line which means we are creating a flask app  instance ( because we will perform all the action use the this flask instance)


@app.route("/")    # this how we write Decorators in Python ( Decorators in any python program is to say before you function is executed the Decorator line must executed first).  
                   # So what does this Decorator line maens?  It to say if someone is trying to run this program it will only return <hellow world> if the person is using a slage < /> 
                   # And we can use decortors to check for authentication i any python program to whoever is try to access our program are they authenticated or not.
def hello():                 # here we are just writing a functionthat when evder someone call it it should return < Hello World>
    return "Hello World"

app.run('0.0.0.0')