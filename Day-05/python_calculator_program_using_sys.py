
# Let Exaplain this programe

# This same program we wrote before But it was HardCoded ( which mean users can not input value on the command line )

# So to do awy with the hard-coding we have to make the program receive argument and read the value by suing the module call < sys > 



import sys                           # before using any module we most import it (both inbuild and PyPi  labrary modules)

def add(num1,  num2):
    add = num1 + num2
    return("Valiue of addition = " + str(add))    # the reason we are using <str>  is because we are addind a sting with a number and for 
                                                 # and for string concantination to happed it most be string + string: we are treating thr number as string here
def subs(num1,  num2):
    sub = num1 - num2
    return("Value of substraction = " + str(sub))

def multi(num1, num2):
    mul = num1 * num2
    return("Value of Multiplication = " + str(mul))

# Seting our code to receive arguments
# NB when ever we pass <sys.argv>  the type of it will be string by default But sine we are using it will number we have to convert
# to have a type as < integer or float > for the application to if not it will give us wrioung answers. 

 
num1 = float(sys.argv[1])              # here pass float is the bast way because if the user passes a number ( whole or decemal ) it will fine

#num1 = int(sys.argv[1])               # But inter will work but will only be able to caculate number that has no decimmal (2.3)
operation = sys.argv[2]

num2 = float(sys.argv[3] )
#num2 = int(sys.argv[3] )

                              # Below  we are calling the function and  passing a condition that if the user pass <add> then 

if operation == "add":       
    output = add(num1, num2)
    print(output)


if operation == "subs":       
    output = subs(num1, num2)
    print(output)


if operation == "multi":       
    output = multi(num1, num2)
    print(output)



#=======================================================>
# BELWO THIS HOW WE RUN THE PROGRAM AND TO SEE THE OURPUT===
#S C:\Users\Samue\python-for-devops\Day-05> python .\python_calculator_program_using_sys.py 2 multi 3
#Value of Multiplication = 6.0

#PS C:\Users\Samue\python-for-devops\Day-05> python .\python_calculator_program_using_sys.py 2 subs 3 
#Value of substraction = -1.0        # thisposible because we are suing <float > type

#PS C:\Users\Samue\python-for-devops\Day-05> python .\python_calculator_program_using_sys.py 2 add 3 
#Valiue of addition = 5.0
#============================================================>