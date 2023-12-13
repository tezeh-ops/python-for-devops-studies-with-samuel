
import sys       # use sys because we will be using the CLI argument

type = sys.argv[1]    # syntax to recive Arg from the CLI

if type == "t2.micro":                   # NB < == > is use to compare  WHILE <= > is the pass a variable
    print("ok, we will create the instance for you")


#=====================================
# How to run it :
# < python .\condition_exmple.py t2.micro >      and the result ==
# ok, we will create the instance for you
#=========================================== This how codition works 

# Let extend our condition ( by passa message if the condition is no made)

else:
    print("your input is not T2.micro,  so we can't create the instamnce")