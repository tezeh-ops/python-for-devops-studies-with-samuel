
# here we are seeing on how to Replace a string within a context or a sentence

# So the Result will be < The quick red fox jumps over the lazy red dog >  so we have replace word < brown > whetrever we see it in the sentence with  the word <red>

import re

text = "The quick brown fox jumps over the lazy brown dog"
pattern = r"brown"

replacement = "red"

new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)
