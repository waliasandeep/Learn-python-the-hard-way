#test Addition
#This program will add all the numbers typed in the arguments
#While dealing with arguments always ignore first one as it is 
# the name of the file

from sys import argv

sum = 0
if len(argv) > 2:
	for i in argv[1:]:
		sum += int(i)
	print "Sum is %d" %sum
else:
	print "Please enter 2 or more numbers!"
