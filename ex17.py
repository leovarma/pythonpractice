from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying content from %r to %r " %(from_file, to_file)
# in_file = open(from_file)
# indata = in_file.read()

indata = open(from_file).read()

print " Input file is of %d bytes long " % len(indata)
print " Does the destination file exists :  %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input( " ? > ")

out_file = open(to_file, 'w')
out_file.write(indata)

print "All done"

out_file.close()
# in_file.close()

copied = open(to_file)
print copied.read()
# in_file.close()
