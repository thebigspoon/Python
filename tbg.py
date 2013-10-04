#Copyrighted Toby Spanton
from string import lower

#Global Variables

global r1I
global r2I
global r3I
global r4I
global r5I
global r6I
global r7I
global u1I
global position
global inventory
global userInput
global bear_1h
global phealth
global u2I
global r8I
global table
global r9I
    
#Variables
phealth = 500
inventory = ['torch']
position = 'room_1'
userName = ''
userInput = ''
moveNorth = 'You can move North'
moveEast = 'You can move East'
moveSouth = 'You can move South'
moveWest = 'You can move West'
r1I = ['']
# r2 = room_2, I = Inventory
r2I = ['gold key','wine']
r3I = []
r4I = ['rock','empty wine bottle']
r5I = []
r6I = ['iron axe', 'sword', 'power of thy epicness']
u1I = []
u2I = ['silver key']
r8I = ['boulder']
r7I = []
r9I = []
bear_1h = 100
table = 'table'

def takeitem(room_inventory):
    global position
    global inventory
    global userInput
    #Remove item from room's inventory and place in the players inventory.
    #check if the item that players wants is in the rooms inventory.
    for item in room_inventory:
        if item in userInput:
            inventory.append(item)
            room_inventory.remove(item)
            print 'You took the item %s' % item

def dropitem(room_inventory):
    global position
    global inventory
    global userInput
    #Remove item fron users inventory and place in the rooms inventory that the players in.
    #Check that you dropped the item.
    for item in inventory:
        if item in userInput:
            room_inventory.append(item)
            inventory.remove(item)
            print 'You dropped the item %s.' % item

def room_check():
    global position
    #Check where the players position is and then run a function for that room.
    if position == 'room_1':
        room_1()
    elif position == 'room_2':
        room_2()
    elif position == 'room_3':
        room_3()
    elif position == 'room_4':
        room_4()
    elif position == 'room_5':
        room_5()
    elif position == 'room_6':
        room_6()
    elif position == 'room_7':
        room_7()
    elif position == 'room_8':
        room_8()
    elif position == 'under_1':
        under_1()
    elif position == 'under_2':
        under_2()
    
def print_check():
    global position
    #Checks the room that the player is in and prints the description of the room.
    if position == 'room_1':
        print '\nYou are standing in a dark and gloomy cave.\nYou can just see the light from the North where the entrance of the cave is.\n%s.' % moveNorth
    elif position == 'room_2':
        print '\nYou have found the Secret Cellar, pretty odd in a cave, maybe this cave is colonised.\n%s' % moveEast
    elif position == 'room_3':
        print '\nYou are in the middle of the cave.\n%s.\n%s.\n%s.' % (moveNorth, moveSouth, moveWest)
    elif position == 'room_4':
        print '\nYou are in the Bears part of the cave.\n%s' % moveEast
    elif position == 'room_5':
        print '\nYou are at the entrance of the cave.\n%s.\n%s.\n%s.\n%s.' % (moveNorth, moveEast, moveSouth, moveWest)
    elif position == 'room_6':
        print '\nYou are at a Junction.\n%s, this leads to a series of underground, man-made, passages.\n%s.\n%s' % (moveNorth, moveWest,moveSouth)
    elif position == 'room_7':
        print '\nThriving is to Lead, you must Lead to Thrive.\n%s.\n%s.' % (moveEast, moveWest)
    elif position == 'room_8':
        print '\nYou are on a dirt road.\n%s.\n%s' % (moveWest, moveSouth)
    elif position == 'room_9':
        print '\nThis path shall lead you to a furious fight, but shall be rewarding.\nGood Luck Knight of the Dark.\nYou arent an adventurer anymore.\n%s.\n%s' % (moveNorth, moveEast)
    elif position == 'under_1':
        print '\nYou are at the start of the passage. There is a lamp on the wall producing light.\n%s.' % moveNorth 
    elif position == 'under_2':
        print '\nYou are in the main area of these passages\nThere is a table in the middle of this open space passage.\n%s.\n%s.\n%s.\n%s.' % (moveNorth, moveEast, moveSouth, moveWest)
        
#Begining of room functions.
def room_1():
    global position
    global userInput
    if not userInput == 'exit':
        if 'north' in userInput:
            position = 'room_3'
        elif 'west' in userInput:
            position = 'room_2'
        elif 'look' in userInput:
            print r1I
        elif 'take' in userInput:
            takeitem(r1I)
        elif 'drop' in userInput:
            dropitem(r1I)
        else:
            print 'That command is invalid.'
            
def room_2():
    global position
    global userInput
    global r2I
    if not userInput == 'exit':
        if 'east' in userInput:
            position = 'room_1'
        elif 'look' in userInput:
            print r2I
        elif 'take' in userInput:
            takeitem(r2I)
        elif 'drop' in userInput:
            dropitem(r2I)
        else:
            print 'That command is invalid.'
            
def room_3():
    global position
    global userInput
    global bear_1h
    global phealth
    global r3I
    if not userInput == 'exit':
        if 'north' in userInput:
            position = 'room_5'
        elif 'south' in userInput:
            position = 'room_1'
        elif 'hit' in userInput:
            if bear_1h == 0:
                position = 'room_4'
                print 'You have over come the bear.'
            elif 'iron axe' in inventory or 'sword' in inventory:
                bear_1h = bear_1h-100
                print 'You succesfully hit the bear.'
            else:
                phealth = phealth-100
                print 'The Bear gets disrupted and attacks you. 100 of your health is gone.'
        elif 'west' in userInput:
            if bear_1h > 1:
                phealth = phealth-100
                print 'There is a Bear. The Bear gets disrupted and attacks you. 100 of your health is gone.'
            elif bear_1h < 1:
                position = 'room_4'
        elif 'look' in userInput:
            print r3I
        elif 'take' in userInput:
            takeitem(r3I)
        elif 'drop' in userInput:
            dropitem(r3I)
        else:
            print 'That command is invalid.'
        
def room_4():
    global position
    global userInput
    global r4I
    if not userInput == 'exit':
        if 'east' in userInput:
            position = 'room_3'
        elif 'look' in userInput:
            print r4I
        elif 'take' in userInput:
            takeitem(r4I)
        elif 'drop' in userInput:
            dropitem(r4I)
        else:
            'That command is invalid.'
        
def room_5():
    global position
    global userInput
    global r5I
    if not userInput == 'exit':
        if 'north' in userInput:
            position = 'room_8'
        elif 'east' in userInput:
            position = 'room_6'
        elif 'south' in userInput:
            position = 'room_3'
        elif 'west' in userInput:
            position = 'room_7'
        elif 'look' in userInput:
            print r5I
        elif 'take' in userInput:
            takeitem(r5I)
        elif 'drop' in userInput:
            dropitem(r5I)
        else:
            print 'That command is invalid.'
            
def room_6():
    global position
    global userInput
    global inventory
    if 'south' in userInput:
        if 'silver key' in inventory:
            position = 'room_9'
        else:
            print 'This door is locked. You need a key.'
    elif 'west' in userInput:
        position = 'room_5'
    elif 'north' in userInput:
        if 'gold key' in inventory:
            position = 'under_1'
            inventory.remove('gold key')
            print 'You enter the passage, the door screaks closed behind you and\nyou hear what seems to sound like rocks tumbling onto the door.'
        else:
            print 'This door is locked. You need a key.'
    elif 'look' in userInput:
        print r6I
    elif 'take' in userInput:
        takeitem(r6I)
    elif 'drop' in userInput:
        dropitem(r6I)
    elif 'ladder' in userInput:
        if 'ladder' in inventory:
            print 'You place the ladder on the what seems to be a boulder, you climb up and get on top, you have a beautiful view of Raybarrow '
    else:
        print 'That command is invalid.'
        
def room_7():
    global position
    global userInput
    global r7I
    if not userInput == 'exit':
        if 'west' in userInput:
            position = 'room_12'
        elif 'east' in userInput:
            position = 'room_5'
        elif 'drop' in userInput:
            dropitem(r7I)
        elif 'take' in userInput:
            takeitem(r7I)
        else:
            print 'That command is invalid.'

        
def room_8():
    global position
    global userInput
    global r8I
    if not userInput == 'exit':
        if 'south' in userInput:
            position = 'room_5'
        elif 'west' in userInput:
            if 'boulder' not in r8I:
                position = 'room_16'
            else:
                print 'There is what looks like a boulder in the way, you need to move it to go through.'
        elif 'look' in userInput:
            print r8I
        elif 'take' in userInput:
            takeitem(r8I)
        elif 'drop' in userInput:
            dropitem(r8I)
        else:
            print 'That command is invalid.'
            
def room_9():
    global position
    global userInput
    global r9I
    if not userInput == 'exit':
        if 'north' in userInput:
            position = 'room_6'
        elif 'east' in userInput:
            position = 'room_10'
        else:
            print 'That command is invalid' 
    
#under = underground room.
def under_1():
    global position
    global userInput
    global u1I
    if not userInput == 'exit':
        if 'south' in userInput:
            print 'That door is blocked by the fallen rocks.'
        elif 'north' in userInput:
            position = 'under_2'
        elif 'look' in userInput:
            print u1I
        elif 'take' in userInput:
            takeitem(u1I)
        elif 'drop' in userInput:
            dropitem(u1I)
        else:
            print 'That command is invalid.'

def under_2():
    global position
    global userInput
    global inventory
    global u2I
    global table
    if not userInput == 'exit':
        if 'south' in userInput:
            position = 'under_1'
        elif 'east' in userInput:
            position = 'under_3'
        elif 'north' in userInput:
            position = 'under_6'
        elif 'west' in userInput:
            position = 'room_5'
        elif 'hit' in userInput:
            if table == 'table':
                print 'You hit the table until you hand gets saw.'
                table = 'saw'
        elif 'saw' in userInput:
            if table == 'saw':
                print 'You saw the table in half.'
                table = 'half'
        elif 'halfs' in userInput:
            if table == 'half':
                print 'Two halfs make a hole.'
                table = 'hole'
        elif 'hole' in userInput:
            if table == 'hole':
                print 'You climb through the hole you made.'
                table = 'finish'
                position = 'room_8'
        elif 'look' in userInput:
            print u2I
        elif 'take' in userInput:
            takeitem(u2I)
        elif 'drop' in userInput:
            dropitem(u2I)
        else:
            print 'That command is invalid.'

#End of room functions.
#On start, asks the name of the user.
userName = raw_input('What is your name adventurer? ')
#Prints the start of the game.
print "\nWell, adventurer %s, there is a deadly force within the midst of a forest of Raybarrow,\nyou must find it and destroy it with your epicness,\nbut first, you must, increase, your Epicness Level...\nThere are several commands that you will want to familiarize yourself with.\nThese commands are highly useful in navigating through the game,\nyou will see these controls after this blurb.\nNow, your mission, should you choose to accapt it,\nis to increase you Epicness Level to 1000, you currently are sitting on 50.\nOnce you have gained all of your Epicness Experiance,\nyou will be notified of this and you will be told\nthe rest of you mission. Good Luck!\nCommands to navigate are very simple, you Have 'North' to go North, 'East' to go East, 'South' to go South\nand 'West' to go West.\nThere are also 'Look' to look around a room for Items, 'S' to view your personal Stats and 'I' to view your Inventory" % userName
#Start of main loop.
while not userInput == 'exit':
    print_check()
    userInput = lower(raw_input('>'))
    if userInput == 'i':
        print inventory
    elif phealth <= 50:
        print '\nYour health is low. You need to eat something or find an infirmary'
    else:
        room_check()