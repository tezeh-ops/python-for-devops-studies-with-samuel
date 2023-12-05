#here we will understand here to write Global and local scop variable

# EXAMPLE 1 Of Global Set Variables.[Here sa we can see we set out Variables Outside the function and the variables can be called from anywhere in our code because there are outside]

a = 10

b = 2 


def addition():                 # here is how we define functions 
    print (a + b)               # herewe are calling the variable from where there are define above


def sub():
    print(a - b )

#To run the functions we need to call them  if not it won't run the functions:

addition()
sub()


# EXAMPLE 2  With Local Scop variable

def addition():            # this here will run because the variable are define within it 
    student = 10
    bags  = 5 
    print(student + bags)

def sub():                    # But this will give us an error because it can't access the Variable of <sudent and bags > define  WHY because is local Scop var 
    print(student - bags)     #  that in with a Function which means it blong only to that Function a lone. 

addition()
sub()
   