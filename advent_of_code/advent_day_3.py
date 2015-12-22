# get input
from day_3_data import data
test = '^^><>>v'

# set up a list/dictionary that contains coordinate values

coordinates = [(0,0)]

x = 0
y = 0

# iterate through all directions and update x/y cooridnates

for direction in data:
	if direction == "^":
		x += 1
	elif direction == ">":
		y += 1
	elif direction == "<":
		y -= 1
	elif direction == "v":
		x -= 1
	coordinates.append((x,y))

# print and profit
print "The final location is: '%s, %s'", x, y, !
print "Sanata delievered %s predents" % (len(set(coordinates)))
