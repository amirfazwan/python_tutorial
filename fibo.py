#!/usr/bin/python

import time


#['1 , 2 ,', '3 , 5 ,', '8 
#, 13 ,', '21 , 34 ,', '55 , 89 ,', '144 , 233 ,']
#
#
#
#
a = 0
b = 1

sequence = []

while True:
	a = b + a
	b = a + b

	#print "a : ",a
	#print "b :",b

	c = "%s , %s ," % (a,b)

	sequence.append(c)

	print sequence
	time.sleep(1)
