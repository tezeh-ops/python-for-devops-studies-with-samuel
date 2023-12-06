# here we are going to make use of the existing code of our calculator that we have written before 

# There file we are going to import to use as module the code is written using FUNCTIONS

# NB we can import a file from anyWhere all we need is justh file path and name  And since are file is in the same place we don,t need a path to it

# the file will be using is the file call < caculator_code_with_function_use.py > 

# METHOD ONE TO IMPORT THE FILE : We import the file and use the name as it's without Changing it 


import caculator_code_with_Function_use

caculator_code_with_Function_use        # calling the file to run it



# METHOD TWO  we import the file and give it aNEW namw by using  keyword < as >  then < NewName >

import  caculator_code_with_Function_use  as  basic_calculation

basic_calculation        # run it we call the file an it will run everting in that file { but we can also riun just a specifict Function in the file using the syntax below}

basic_calculation.addition()                               # We use this if we want to invoke just a paticular FUNCTION without call everthing in the file 
                                # but in this demo it will print out <addtion value  2 times WHY because in the Origin file we have < print > statement in it 
                                # But in real word we will not but using < print > BUT < return > and this < basic_calculation.addition() >  will work  perfectly


# NB  and of the methos above will give us this result:
#==========================================>
#Valiue of addition = 15
#Value of substraction = 5
#Value of Multiplication = 50
#=============================================>>