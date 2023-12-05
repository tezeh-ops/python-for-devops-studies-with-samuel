import re

text = "apple,banana,orange,grape"    
pattern = r","                               # trying to split the string above from whereever it sees commal<, > 

split_result = re.split(pattern, text)
print("Split result:", split_result)     # when run the result will be someting like < Split result: ['apple', 'banana', 'orange', 'grape'] >
