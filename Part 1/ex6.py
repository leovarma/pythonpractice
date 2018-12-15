# -- coding: utf-8 --


print " ------------------------------------------------------------------"
x = "There are %d types of people" % 10 # Declaring a string to x
binary = "binary" # Assigning binary to variable binary
do_not = "don't" # Assigning don't to do_not
y = "Those who know %s and those who %s."  % (binary, do_not) # Declaring string y and Assigning a stiring
print x # print x string
print y # print y stiring

print "I said : %r." % x # Concatenate inline string with x
print "I also said : '%s' ." % y # Concatenate inline string with y

hilarious = False # boolean value False is assigned to hilarious variable
joke_evaluation = "Isn'that joke funny ? ! %r" # Assigning a string to joke_evaluation
print joke_evaluation % hilarious # Concatenating two strings

w = "This is left side of a stiring" # Declare w
e = " ... to the right side of the same string" # Declare e

print w + e # Concatenate w & e
print " ------------------------------------------------------------------"
