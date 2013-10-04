#Copyright Toby Spanton 2013
global position

position = 'room_1'
userName = ''

def location(position):
    while 'room_1'==position:
        print 'You are standing in a dark and gloomy cave. You are at the end with a continuing of the cave to the North'
    
userName = raw_input('What is your name adventurer? ')
print "Well, adventurer %s, there is a deadly force within the midst of the forest, \nyou must find it and destroy it with your epicness, \nbut first, you must increase your epic level..." % userName

while not userInput == 'exit':
    location
    userInput = raw_input('>')