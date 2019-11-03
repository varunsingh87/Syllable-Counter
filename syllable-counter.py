import re
word = input("Enter a word to find the syllable count: ")
regex = r"([^aeiouy])(a|e|i|o|u|y)"
matches = re.findall(regex, word, re.MULTILINE)
print(len(matches))