from day_5_data import data

test = data 


total_rows = 0
nice_rows= 0
naughty_rows = 0
vowels = set("aeiou")
bad_combos = ["ab", "cd", "pq", "xy"]



for row in test.split("\n"):
	rule_1_check = False
	rule_2_check = False
	rule_3_check = True
	#print row
	# checks rule 1, at least 3 vowels 
	vowel_counter = 0
	for letter in row:
		if letter in vowels:
			vowel_counter += 1
			if vowel_counter >= 3:
				rule_1_check = True
				
				break
	#now check rule 2, two letters in a row
	for i in range(1,len(row)):
		if row[i] == row[i-1]:
			#print("has double letters!")
			rule_2_check = True
			break
	# check rule 3, bad combos
	for combo in bad_combos:
			if combo in row:
				#print "this has bad letters!"
				rule_3_check = False
				break
	if rule_1_check and rule_2_check and rule_3_check:
		#print "huzzah!"
		nice_rows += 1
	else:
		naughty_rows += 1
	total_rows += 1

print "bad rows = ", naughty_rows
print "good rows = ", nice_rows
print "total rows = ", total_rows






# print total_rows
# print nice_rows
# print naughty_rows




