def add(a, b):
    print "ADDING %d + %d" %(a,b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" %(a,b)
    return a - b

def multiply(a, b):
    print "MULTIPLING %d * %d" %(a,b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" %(a,b)
    return a / b

print "Lets do some math with funtions"

age = add(23, 32)
height = subtract(89, 12)
weight = multiply(2, 60)
iq = divide(88, 23)

print " AGE : %d, HEIGHT : %d, WEIGHT : %d, iq : %d ." %(age, height, weight, iq)

print "Hers's a puzzle, "
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print " That's becomes: ", what , "Can you do it by hand ?"
