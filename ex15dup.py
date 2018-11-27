from sys import argv

script, filename = argv

text = open(filename)
print text.read()
text.close()

new = raw_input("Enter another file name : ")
newfile = open(new)
print newfile.read()
newfile.close()
