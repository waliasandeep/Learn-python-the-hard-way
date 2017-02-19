#Excersice 18

#this function is the most interesting because of it's arguments
#First we take a *args(list of arguments) which works like (script,arg1 = argv)
# We have to unpack the arguments
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
	print "arg1: %r" % arg1

def print_none():
	print "I got nothin'."


print_two("Sandeep", "Walia")
print_two_again("Sandeep", "Again")
print_one("Howdy")
print_none()
