#Exercise 24
print "Let's practise everything"
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs'

poem = """
\tThe loovely world
with logic so firmly planted 
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none
"""

print "----------------"
print poem
print "----------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

start_point = 10000
#This is an interesting way to get values from the a function
#A python function can return more than one variables
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates" % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
#As shown here the returned values can be directly printed in python
print "We'd have %d beans, %d beans, and %d crates" % secret_formula(start_point)