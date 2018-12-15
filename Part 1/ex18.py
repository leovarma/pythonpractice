# this one is like your scripts eith argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1 : %r , arg2 : %r" % (arg1,arg2)

# OK, *args is point less, we can just do this
def printwo_again(arg1, arg2):
    print "arg1 : %r , arg2 : %r" % (arg1,arg2)

#this takes just one argument
def one_arg(arg1):
    print "arg1 : %r " % arg1

#this takes no arguments at all
def no_arg():
    print "I got nothing"

print_two("Vasrma", "Sruthi")
printwo_again("Sruthi", "Agastya")
one_arg("Varma")
no_arg()
