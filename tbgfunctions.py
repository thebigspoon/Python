position = 'room_1'
moveNorth = 'You can move North'
moveEast = 'You can move East'
moveSouth = 'You can move South'
moveWest = 'You can move West'
    
def printing():
    if 'room_1' == position:
        print '\nYou are standing in a dark and gloomy cave.\nYou can just see the light from the North where the entrance of the cave is.\n%s.' % moveNorth
    elif 'room_2' == position:
        print '\nYou are in the middle of the cave.\n%s.\n%s.\n%s, but there is a giant rat in the way.' % (moveNorth, moveSouth, moveWest)
    
def room_1():
    if userInput == 'North':
        position = 'room_2'
    else:
        print 'That command is invalid'
        
def room_2():
    if userInput == 'North':
        position = 'room_3'
    elif userInput == 'South':
        position = 'room1'
    elif userInput == 'West':
        position = 'room_4'
    else:
        print 'That command is invalid'