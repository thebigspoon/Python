#Copyright Toby Spanton 2013

def print_room():
    global position
    if position=='room1':
        print "You are in the Basement, there is a door to the East."
    elif position=='room2':
        print "You are in the Panic Room. Don't panic."
    else:
        print "I don't understand."
        
def room_1(user_input):
    global position
    if 'East' in user_input:
        position = "room2"
    else:
        print "What the..."
        
def room_2(user_input):
    global position
    if 'West' in user_input:
        position = "room1"
    else:
        print "What the..."