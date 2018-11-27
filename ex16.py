from sys import argv

script, filename = argv

print " We are going to erase %r. " % filename
print " If you don't want to delete the file, hit CTRL + C. "
print " If you do want that, hit RETURN . "

raw_input(" ? ")

print "Opening the file"
target = open(filename, 'w')

print "Truncating the file. Goodbye "
target.truncate()

print "Now i'm going to ask you three line, "

line_1 = raw_input("Input Line 1 : ")
line_2 = raw_input("Input Line 2 : ")
line_3 = raw_input("Input Line 3 : ")

print " Now I'm writing this lines to the file"
target.write(line_1 + "\n" + line_2 + "\n" + line_3 )
# target.write("\n")
# target.write(line_2)
# target.write("\n")
# target.write(line_3)
# target.write("\n")
target.close()

fileopen = open(filename)
print fileopen.read()
