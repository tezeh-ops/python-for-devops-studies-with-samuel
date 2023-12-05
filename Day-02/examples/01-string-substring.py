
# here we are power of <substring > fo find a word in the context. 

# so here we have dcefine a string variable as < Python is awesome > 

# And we have define a < substring = "is" > we are using the subsgtring to see it the word waht we are looking for exist in the < Python is awesome > and if it does

# it will print us thye message < found in the text > == < is found in the text >

# And is the substring does not exist it will execute and it will not give us any message

text = "Python is awesome"
substring = "is"
if substring in text:
    print(substring, "found in the text")
