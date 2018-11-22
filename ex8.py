formatter = "%r %r %r %r"

print "=" * 130


print formatter % (1,2,3,4)
print formatter % ('one', 'two', 'three', 'four')
print formatter % (True, False, True, False)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % ("Hello World", "Practice Python", 'Hello Varma', 'Hello Agastya')
print "=" * 130
