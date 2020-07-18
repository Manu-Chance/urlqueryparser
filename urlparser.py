#############################################################

#!/bin/env python3

# Attempt to solve URL Query Parser challenge from Discord
# more information in README.md

#############################################################

list1 = []						# Setting initial variables
pos = -1
condition = False
displayPos = 0

weblink = input("Please enter a link to parse:> ")	# Take user input (the link they want to parse)


for letter in weblink:					# Go through each iteration of the user string

	if letter == '?':				# condition to detect special keywords
		condition = True			# enable appending of letters
		pos += 1				# element position (new iteration)
		list1.append("")			# create new element position
		continue;				# prevents continuation of special keywords

	if letter == '&':				# view above (line 20 - 24)
		condition = True
		pos += 1
		list1.append("")
		continue;

	if letter == '=':				# view above (line 20 - 24)
		condition = True
		pos += 1
		list1.append("")
		continue;


	if condition == True:				# set to false until the first special keyword
		list1[pos] = list1[pos] + letter	# append the letter to the element


list1.append("")					# prevent errors when parsing weird links
objRange = (pos // 2) + 1				# calculates the length of the next for loop (2 elements per line)


for i in range(objRange):				# prints all elements in certain pattern
	print(list1[displayPos] + " : " + "\""  + list1[displayPos + 1] + "\"")
	displayPos += 2					# keeps track of element pos
