from sys import argv

script, input_file = argv                       # Assiging arguments from the script

def print_all(f):                               # Defining function that reads a file, which is passed through an argument
    print f.read()

def rewind(f):                                  # Setting the sursor position to the starting
    f.seek(0)

def print_a_line(line_count, f):                # Functoin that prints the mentioned line from the passed file
    print line_count, f.readline()

current_file = open(input_file)                 # Set the opened file object to 'current_file'

print "First lets print the whole file \n"
print_all(current_file)                         # Calling functoins

print "Lets rewind, kind of tape."
rewind(current_file)

print "Lets print three lines. \n"

current_line = 1
print "Position of the cursor is at %d line. \n" %current_line
print_a_line(current_line, current_file)

current_line = current_line + 1
print "Position of the cursor is at %d line. \n" %current_line
print_a_line(current_line, current_file)

current_line = current_line 
print "Position of the cursor is at %d line. \n" %current_line
print_a_line(current_line, current_file)


print_a_line(current_line + 1, current_file)
print "Position of the cursor is at %d line. \n" %current_line
