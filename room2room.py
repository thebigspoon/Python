#Copyright Toby Spanton 2013
global position
def print_room():
    global position
    if position=='room1':
        print "You are in the Basement, there is a door to the East."
    elif position=='room2':
        print "You are in the Panic Room. Don't panic."
    elif position=='room3':
        print "You are in the classroom. there"
    else:
        print "I don't understand."
        
def room_1(user_input):
    global position
    if 'East=' in user_input:
        position = "room2"
    else:
        print "What the..."
        
def room_2(user_input):
    global position
    if 'West' in user_input:
        position = "room1"
    else:
        print "What the..."
def room_3(user_input):
    global position
    if 'East' in user_input:
        if position == 'room2':
            position = 'room3'
    else:
        print "What the..."

position = 'room1'
user_input = ''

while input <> 'Exit':
    print_room()
    user_input = raw_input('>')
    if position == 'room1':
        room_1(user_input)
    elif position == 'room2':
        room_2(user_input)
    elif position == 'room3':
        room_3(user_input)