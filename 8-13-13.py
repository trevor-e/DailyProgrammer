from collections import deque
import sys

amount = int(raw_input("Amount of words: "))
words = []
longest = 0

#Read in the words and create queues of them
for x in range(amount):
	temp = str(raw_input()) #take in the word
	if len(temp) > longest:
		longest = len(temp) #update the longest string size
	words.append(deque(temp)) #add as a list of characters

print " " #formatting

#Loop using the longest word size as the bound and pop characters off each queue
for x in range(longest):
	for y in range(amount):
		if len(words[y]) > 0:
			sys.stdout.write(words[y].popleft())
		else:
			sys.stdout.write(" ")
	sys.stdout.write("\n")
