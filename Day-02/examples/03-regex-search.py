import re

text = "The quick brown fox"
pattern = r"brown"                             # search the word < brown > in the string above

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")
