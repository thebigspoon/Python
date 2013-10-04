# Variable with a string inside.
x = "There are %d types of people." % 10
# Variable.
binary = "binary"
# Another Variable.
do_not = "don't"
# Another Variable with strings attached.
y = "Those who know %s and those who %s." % (binary, do_not)

# Print the variable that I declared of which is X.
print x
# Print the variable that I declared of which is Y.
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with the right side."

print w + e