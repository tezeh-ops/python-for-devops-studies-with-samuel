#below is a somme simple example of of a sting that has a name and we jut want to fetch just the username < johndoe> out of the string 


arn = "arn:aws-cn:iam::123456789012:user/johndoe"

arn.split("/")                          # here we are the string above in to Two so that it should be in oa form of a list and can easily index it and id we split it the 
                                        # will be < ['arn:aws-cn:iam::123456789012:user', 'johndoe'] > and we this we can now insex it as [0] or [1] depending on what we want
print(arn.split("/")[1])

# the we can run it and the ourput should be < johndoe> if we change [1] to  [0] the out put will be <arn:aws-cn:iam::123456789012:user >


# Example  2  here we define a string namev as <samuel> and we will try ti change the name from lowcase to uppercase 

name = "samuel"

print(name.upper())     # the we can execute



# Example 3
#v here we declare two str and we want to print str 1 plust stri 2 and we waht space inbetween them and for that we will be using <" " >  ( douple qoutes)

str1 = "Hello"
str2 = "World"
result = str1 + " " + str2    # this call String cancatination  [ cancatination in python is simple just adding two or more strings]
print(result)

# when ran the out will be < Hello  World >