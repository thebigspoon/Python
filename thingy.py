data = ["kahuna","loopy","noggin","dingy","waddle","canoodle","shebang"]
task = "anything"
import random
while not task == "end":
	print "pick task: 1, 2, 3, 4, 5, 6, 7, 8, 9 or end"
	task = raw_input()
	if task == '1':
		print data[:2]
	elif task == '2':
		print data[3:4]
	elif task == '3':
		print data[::2]
	elif task == '4':
		print data[-2]
	elif task == '5':
		print data
	elif task == '6':
		print "Please enter a random word."
		jacob = raw_input()
		data.append(jacob)
	elif task == '7':
		print data[::-1]
	elif task == '8':
		print sorted(data)
	elif task == "9":
		print random.shuffle(data)
	#if wrong input loop back
	#and ask again
	#task 5
	#print each word in data
	#task 6
	#get new word from user to add to data
	#task 7
	#print data in reverse
	#task 8
	#order data alphabetically
	#task 9
	#print random
	#task 10
	#print random number of random words