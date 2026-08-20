#What is a Regular Expression?
#Regular expressions (often abbreviated as regex) provide a concise, flexible language for matching, searching, and extracting specific patterns of text within strings.

#To use regular expressions in Python, you must first import the built-in module: import re

#re.search(pattern, string): Returns True or False depending on whether the pattern matches anything in the target string (similar to string .find()).

#re.findall(pattern, string): Extracts and returns a list containing all matching substrings.

#Fine-Tuning Matching
#When extracting or searching through data, broad patterns can lead to unexpected matches (false positives). Fine-tuning your regular expressions allows you to restrict matching strictly to lines or strings that meet specific structural requirements.

#Matching and extracting
import re
x = 'My 2 favorite number are 19 and 42'
y = re.findall('[0-9]+', x) #[0-9]+ - one or more digits
print(y)

y = re.findall('[AEIOU]+', x)
print(y)

y = re.findall('[a-z]+', x)
print(y)

y = re.findall('[a-z or A-Z]+', x)
print(y)

