tabby_cat = "\tI'm tabbed in"
persian_cat = "I'm split \non a line"
backslash_cat = "I'm \\a\\ cat"

fatcat ="""
I'll do a list :
\t * Cat food
\t * Fishies
\t * Catnip\n\t * Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fatcat
print "''"
print '''



while True:
    for i in ["/","-","|","\\","|"]:
         print "%s\r" % i,
