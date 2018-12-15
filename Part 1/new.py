from sys import argv

script, filename = argv

file = open(filename)
print file.read()
file.close()

newfile = open(raw_input("Enter another file : "))
# newfile.open()
print newfile.read()
newfile.close()
