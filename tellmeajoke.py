#python 2.7.2
# "tell me a joke" program

#import functions here
from jokes import *
from random import randint

#main program

#global varibles
name = ''
count = 0 #number of jokes told
input = ''
numberOfJokes = 2 #change this as you add more jokes

#loops until user types no
while(not input == 'no'):
    print
    if count <=0:
        print "Would you like to hear a joke?"
    else:
        print "Would you like to hear another joke?"
    input = raw_input()
    if input == 'no':
        print "OK, goodbye"
        #then exit
    else:
        n = randint(0,numberOfJokes)
        if n == 1:
            count += knockknock()
	elif n == 2:
			count += funfun()
        else:
            print "too bad"