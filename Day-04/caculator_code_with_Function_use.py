
# Here we will be using FUNCTIONS in our Code

#ADVANTAGE OF USING FUNCTIONS IN OUR CODE

#-1  Readability of the code ( easy to read and track erros)
#-2  Reusability (modularity)
#-3  Debugging ( which function make easy to tackel the exact funtion that is not working anf fix it )

num1 = 10
num2 = 5 

def addition():
    add = num1 + num2
    print("Valiue of addition = " + str(add))

def substraction():
    sub = num1 - num2
    print("Value of substraction = " + str(sub))

def multiplication():
    mul = num1 * num2
    print("Value of Multiplication = " + str(mul))


# NB before we can run our function we have call the FUNCTION  withthier names if not python will not understand or give you any output:

addition()
substraction()
multiplication()