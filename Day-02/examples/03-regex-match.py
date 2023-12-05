
# here we see what happen when we use < match > to de search in a context or in string.

# the code we are seeing below where trying to look for the word < quick > in the string of < text> But as wee can see the word <quick > exist and on normal Circumstances

# we think the Result should be < Match Found >  But No the result will instaed be < No match > WHY?

# When we use < match > to look for a string ot word in a sentence it ONLY LOOK FOR THE WORD AT THE BEGINING OF THE string/sentent:

# It only compare the word we want with first word in that string an d if the word is not the first word it will say not word  found even if the word exist in the sentence somewhere

# So we want to look for the word everywhere we need to change < match > TO <search >  and it will look for the word all-over

import re

text = "The quick brown fox"
pattern = r"quick"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")



#Below is an Example of using <search>  instaed of <match > and the Result will be < Match found >

import re

text = "The quick brown fox"
pattern = r"quick"

search = re.search(pattern, text)
if search:
    print("Match found:", search.group())
else:
    print("No match")
