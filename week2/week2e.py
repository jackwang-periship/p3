from sys import argv

script, filename = argv
txt = open(filename)
print "Here's your file %r:" % filename
print "Anything between the asterisk line is the read out of the file"
print "********************************************************"
print txt.read()
print "********************************************************"
print "Type the filename again:"
file_again = raw_input("> ")
txt_again = open(file_again)
print txt_again.read()