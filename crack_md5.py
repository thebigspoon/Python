# -- coding: utf-8 --
#!/usr/bin/python

#Get MD5 of user input
#write algorithm to crack md5, and report how long it took

import md5
from itertools import product

#function to check if item
def check_hash(item,toBeCracked,count):
    hash = md5.new()
    hash.update(item)
    if hash.digest() == toBeCracked:
        print "Cracked in %r iterations" % count
        return True
    return False

#bruteforce function
#returns true if cracked
def brute_md5_old(toBeCracked):
    #brute force through every letter combination
    #and test against hash - print how long it takes
    count = 0
    hash = md5.new()
    length = 8 #length of word to be cracked
    #character list to check'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    my_list= 'abcdefghijklmnopqrstuvwxyz'
    
    for n in range (1,length):
        test = product(my_list, repeat=n) #not sure of cost of this?
        count = count + (len(my_list))**n
        for a in test:
            count += 1
            item = ''.join(a)
            #print item
            if(check_hash(item,toBeCracked,count)):
                return True
    return False

def brute_md5_v2(toBeCracked):
    #brute force through every letter combination
    #and test against hash - print how long it takes
    count = 0
    hash = md5.new()
    length = 8 #length of word to be cracked
    #character list to check'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    my_list= 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    
    for a in my_list:
        if(check_hash(a,toBeCracked,count)):
            return True
        for b in my_list:
            if(check_hash(a+b,toBeCracked,count)):
                return True
            for c in my_list:
                if(check_hash(a+b+c,toBeCracked,count)):
                    return True
                for d in my_list:
                    if(check_hash(a+b+c+d,toBeCracked,count)):
                        return True
                    for e in my_list:
                        count += 1
                        if(check_hash(a+b+c+d+e,toBeCracked,count)):
                            return True
    return False


#get input from user
print "type a word to crack."
input = raw_input()
#generate md5 hash of user input
toCrack = md5.new()
toCrack.update(input)
#print md5 hash that will be cracked
crack = toCrack.digest()
print "md5 hash is: ", crack
print "Choose algorithm. new or old?"
input = raw_input()
if input == "new" or input == 'n':
    solved = brute_md5_v2(crack)
else:
    solved = brute_md5_old(crack)
print "solved: ", solved





