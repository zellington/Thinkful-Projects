# get input
from day_3_data import data
	#test = '^v^v^v^v^v'

# set up santa and robo_santa variables as lists

	#test_list = list(test)
move_list = list(data)

santa = [(0,0)]
robo_santa = [(0,0)]

total_moves = [(0,0)]

# santa moves with x and y, robo_santa moves with robo_x and robo_y
x = 0
y = 0
robo_x = 0
robo_y = 0

# # iterate through santa's directions (even moves)

for move in move_list[0:][::2]:
	if move == "^":
		x += 1
	elif move == ">":
		y += 1
	elif move == "<":
		y -= 1
	elif move == "v":
		x -= 1
	santa.append((x,y))
	
# robo_santa's moves
for robo_move in move_list[1:][::2]:
	if robo_move == "^":
		robo_x += 1
	elif robo_move == ">":
		robo_y += 1
	elif robo_move == "<":
		robo_y -= 1
	elif robo_move == "v":
		robo_x -= 1
	robo_santa.append((robo_x,robo_y))

total_moves = len(set(santa + robo_santa))

# # print and profit
# test print statements
# print "the data had this many total moves", len(data)
# print "Santa made this many moves", len(santa)
# print 'robo santa made this many moves:', len(robo_santa)
#print "total moves are:", len(total_moves)
#print "The final location for santa is: '%d, %d'", (x, y)
#print "The final location for robo_santa is: '%d, %d'", (robo_x, robo_y)

print "Together, they visited", total_moves ,"houses"