# setting up var withoout making use of a list

sudent1  = "sam"
sudent2  = "peter"
sudent3 = "amos"
sudent4  = "tez"
# Calling the var to print out the names 
print(sudent1)
print(sudent2)
print(sudent3)
print(sudent4)

#  AS we can see above thta without using list it become tedious to  write te code and alot of repeatition
#=================================================================================================================>>

# Using list now 

students_names = ["sam",  "joel", "peter", "john"]    # now we see with list is so easy to use list.
# print(type(students_names))                       # we cant put <type> just find what kind of var it's (e.g  a list or tuple )

# how to add more element in out list:
students_names.append("oppor")   # when print it we add the new sudent name in tje list
# let see haow to remove an element (let take out <peter):
students_names.remove("peter")

# how can i print just only one/specific lement in the list ( taht is where <ndexing > comes in):

print(students_names[0])            # here is how indexing works

# how to know the let of your list:

print(len(students_names))    # it will give us <4> because that is the number of element we have in our list

# let see how we can crete a new list from another list:  and the output should be = ['sam', 'joel', 'john'] 
# Nb= i knoew that we may if surpose to be < 4> element but y just < 3> The reson is that the upper elementwil not be printed so it < 0, 1 , 2 > so <3> is not include 


#print(students_names[0:3])          # this one method  OR we can do 

new_student_list = students_names[0:3] 
print(new_student_list)


# let see how we can Concantinate the the string in our list:

print(students_names[0] + " "+  students_names[1])    # and the result == <sam joel >



print(students_names)

#========================================================================

#Example -2 of list
#1= Let say we have a list of numbers that we want to ply with:

numbers = [1, 20, 10, 15 ]   # at this point we can see the numbers are not in order so how can we put them in order:

# to rearrange the number =

numbers.sort()          # using <sort> to rearrange 

print(numbers)      # when print the result will be = [1, 10, 15, 20]

#==========================================================================>

#Example-3
# here we will be creating alist that contain <strings, inter,  float >

random_list = [1, 2, 3,  "abi", "ram", 7.6]   

print(random_list[5])

print(random_list) # this will print withour any error Because list tread everything in it as ELEMENT 

