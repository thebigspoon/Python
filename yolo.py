print "Enter the Height you would like you Pyramid to be!"
height = int(raw_input())

for n in range(1,height):
    print ' ' * (height-1-n) + '#' * (n * 2 - 1)