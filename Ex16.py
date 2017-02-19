#Exercise 16 More File manipulation

filename = raw_input("Enter the file name")
print "We are going to erase the file %r" %filename
print "If you want to abort hit Ctrl-C"
print "If you want to hit RETURN"

raw_input("?")

print "Opening the file"
#This is how we open a file to write
target1 = open(filename,'r')
target = open(filename,'w')
print target1.read()
#print "Now we are truncating the file"
# There is no need to truncate the file as when we open a file 
#using open(filename,'w') it automatically truncates the file 
#target.truncate()

print "Enter new lines"

line1 = raw_input("line1:")
line2 = raw_input("line2:")

target.write(line1 + "\n")
target.write(line2)

print "Now the new contents are :"  
target.close()
