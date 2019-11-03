import re
word = input("Enter a word to find the syllable count: ")
regex = r"([^aeiouy])(a|e|i|o|u|y)"
matches = re.findall(regex, word, re.MULTILINE)
count = len(matches)
if ['a', 'e', 'i', 'o', 'u'].__contains__(word[0]):
    count+=1
print(count)