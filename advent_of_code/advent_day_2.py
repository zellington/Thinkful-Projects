
from day_2_data import data 


# total = 0	

# for row in data.split('\n'):
# 	l,w,h = [int(x) for x in row.split('x')]
	
# 	total += ((2*l*w + 2*w*h + 2*h*l)+min((l*w), (w*h), (h*l)))

# print "the total is:" , total


# --DAY 2 Part 2 Solution


test = '''1x1x10
20x3x11
15x27x5
6x29x7'''
# 15x27x5
# 6x29x7'''

count_feet = 0	

for row in data.split('\n'):
	l,w,h = [int(x) for x in row.split('x')]
	bow = (l*w*h)
	print "the bow is: ", bow
	ribbon = (2*(min((l+w),(w+h),(l+h))))
	#ribbon = ribbon_list.append(l)
	print "the ribbon is: " , ribbon
	count_feet = (count_feet+ribbon+bow)
	print "the count is:", count_feet
# 	total_ribbon = bow+ribbon
# 	print "the total_ribbon is: " , total_ribbon
# 	count_feet = count_feet + total_ribbon
print "the final total is: ", count_feet

