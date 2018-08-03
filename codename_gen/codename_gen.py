# import module random, the following command is the first st.
import random
import datetime

#set the file as variable 'adjective or noun'
# Creating variable for adjetives
adjectives = '/home/joshua/project/adjectives.txt'
ADJ = open(adjectives).read().splitlines()

# Creating variable for nouns
nouns = '/home/joshua/project/nouns.txt'
NOUN = open(nouns).read().splitlines()

print random.choice(ADJ) + ' ' + random.choice(NOUN) + ' ' +  datetime.datetime.today().strftime('%Y%m%d')
