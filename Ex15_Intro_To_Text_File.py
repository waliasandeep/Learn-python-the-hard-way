# Exercise 15
from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" %filename
print txt.read()
#!!Always close a file after opening
txt.close()
#.read function will read the file after opening
#Thus to read a file First open it
# and then use .read() function to read it

print "Type the file name again:"
file_again = raw_input("> ")

txt_again = open(file_again)
print txt_again.read()
txt_again.close()
