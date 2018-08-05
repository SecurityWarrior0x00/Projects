import re

bible = open("regex.txt", "r")
regex = re.compile(r'\d{3}\w{3}')

for line in bible:
    four_letter_words = regex.findall(line)
    for word in four_letter_words:
        print word