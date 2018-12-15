def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d of cheeses." %cheese_count
    print "You have %d of cracker boxes. " % boxes_of_crackers
    print "Man that's enough for a party"
    print "Get a blanket. \n"

print "We can give the numbers directly"
cheese_and_crackers(20, 30)

print "Or we can use the varialbes from our script "
amount_of_cheese = 10
amount_of_boxes = 50

cheese_and_crackers(amount_of_cheese, amount_of_boxes)

print "We can do math inside"
cheese_and_crackers(10+20, 45+35)

print "We can also combine numbers and variables"
cheese_and_crackers(amount_of_cheese + 90, amount_of_boxes + 20)

cheese_num = int(raw_input("Enter value of cheese count : "))
boxes_num = int(raw_input("Enter value of boxes count : "))
cheese_and_crackers(cheese_num, boxes_num)
