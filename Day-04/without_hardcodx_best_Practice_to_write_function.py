
# here we are trying to make our Function more flexiable  and this will increase the Modularity of our Functions 

# here we taking out the hard-coding of the function by not defining any Var  e.g  ( sum1 = 10 )> . And this will help any one to reuse ourcode


#NB  Here is the best way ro write our functions


def addition(num1,  num2):
    add = num1 + num2
    return("Valiue of addition = " + str(add))

def substraction(num1,  num2):
    sub = num1 - num2
    return("Value of substraction = " + str(sub))

def multiplication(num1, num2):
    mul = num1 * num2
    return("Value of Multiplication = " + str(mul))


# NB before we can run our function we have call the FUNCTION  withthier names if not python will not understand or give you any output:

print(addition(10, 5))
print(substraction(10, 5))
print(multiplication(10, 5))


