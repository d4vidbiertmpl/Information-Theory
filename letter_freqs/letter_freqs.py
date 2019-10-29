import math
import string
import collections

import numpy as np

# open the input file, which was added as input.txt in the menu on the left.
f = open("Jack.txt")

# read the text in the file (it is stored as a long string), and convert it to lowercase in the process
data = f.read().lower()

letter_counter = collections.Counter()

# loop through all characters in the file:
total_letters = 0
for c in data:
	if ord(c) in np.arange(ord('a'), ord('z')+1):
		letter_counter[c] += 1
		total_letters += 1

for uni_c in np.arange(ord('a'), ord('z')+1):
	letter = chr(uni_c)
	letter_count = letter_counter[letter]
	frequency = np.round(letter_count/total_letters, 4)
	print("Letter {}: {} times, thats {} percent of the total.".format(letter, letter_count, frequency))

mf_letter = letter_counter.most_common(1)[0][0] if letter_counter else None
print("The most frequent letter is: {} with {} occurences.".format(mf_letter, letter_counter[mf_letter]))