print 'Welcome to Fizz Buzz!'

x = int(raw_input("How high would you like to count?:"))
y = x + 1
for i in range(y):
	if i % 3 == 0 and i % 5 == 0:
		print "fizz buzz"
	elif i % 3 == 0:
		print "fizz"
	elif i % 5 == 0:
		print 'buzz'
	else:
		print i

print "That's it - thanks for playing!"