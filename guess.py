guesses = 0
import random 
number = random.randint(1,15)

print "Hi there, What is your name?"
myName = raw_input()
print "Well, I am Le Guessing Game, now %s," % myName
while guesses < 5:
	guess =  int(raw_input("Please guess a number between 1-15:"))
	guesses +=1
	if guess < number:
		print "Guess is to low. Try again."
	elif guess > number:
		print "Guess is to high. Try again."
	elif guess == number:
		print "Congrats %s, You guessed my secret number in %s goes. AWESOME" % (myName, guesses)
		break