
# Let see how we can use loops to print some a lot of time with keep rewriting the code:

print("samuel") # if we do this it will print < samuel> just once. What if wee need samuel to be printer 100 time?
# that we have to write 100 time which is too much and not good but using loop it makes it easy :
#======================================================================================>>>


#EXAMPLE USING LOOP

for i in  range(10):    # we are saying in the range of 0-9 print <sam  munoh > And it did print it 10 times
    print("sam  " "  munoh")
    print("Tezeh")


#=================================LET Understand the Keywords we have use above = < for,  in ,  range > ================>

# < for > stands for <for loop > type.  And we use <FOR LOOP> when we know the number of time we want that loop to run E. < 2, 10 , 1000,000 times etc
# And syntax for <For Loop> start with the key word == <for >  and follow by any variable of your choose: e.g above we use < i > 
# And we will use a pacticular sequence and between the VARIABLE  and SEQUENCE we will use another keyword call < in > 
# So the Sequence here as seen above is = range(10) which will return a list from < 0- 9 > 

# <range> return the specific element/numbers

# NB in Python FOR LOOP execute againts SEQUENCE because it can be definate (specific) <list, tuple, string, range >

# How do we know the some variables behind the seen [ As i said the <i> above can be anythin but it represent a Variable the point to the number of
#  time the the loop will run which will be from < 0 - 9] to see tis number let out the variable:

    print(i)    # this will print to us < 0 - 9 >

#========================================================>>


#Example-2

for sam in  range(15):    # we are saying in the range of 0-14 print <sam  munoh > And it did print it 10 times
    print(sam)            # since i use <sam> as my <var/indicator> here it output the number < 0-14 > which is the number of time <Tezeh > will be printed
    print("Tezeh")

#========================

#  So  foe better understanding of the syntax ==

# < for  Variable  in Sequence: >  ==  < for ty in range(20): >

# Thre are three this that can go/represent the SEQUENCE : < range,  List,  Tuple  >

#==========================================================================>>


 # EXAMPLE using loop with LIST

colors = ["yello", "green", "blue"]

for x in colors:
    print(x)        # this will print our various colors
