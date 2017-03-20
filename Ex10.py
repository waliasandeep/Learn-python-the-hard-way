#Exercise 10
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split \non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list
\t* Cat Food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# test
#"""%r will print everything raw and no escape sequence will come into effect while
#using them
print "test %r \n" %fat_cat
"""
input
print "test %r \n"%fat_cat
output
test "\nI'll do a list\n\t* Cat Food\n\t* Fishies\n\t* Catnip\n\t* Grass\n"
input
>>> print "test %s \n"%fat_cat
output
test
I'll do a list
        * Cat Food
        * Fishies
        * Catnip
        * Grass
