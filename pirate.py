import random 

questions = {
	"strong": "Do you like yer drinks strong?",
	"salty": "Do ye like 'em with a bit 'o salt?",
	"sweet": "Would you like a drink as sweet as you, dahhhrrrrrlin?",
	"bitter": "Think they're better bitter, my friend?",
	"dry": "How 'bout one dry as a desert?",
}
ingredients = {
    "strong": ["the kraken", "Don Q Gold", "splash o gin"],
    "salty": ["pickle juice", "salt-dusted rim", "candied bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of orange zest"],
    "sweet": ["agave", "spoonful of honey", "grenadine"],
    "dry": ["splash of triple sec", "dash of cassis", "slice o melon"]
}

def your_order():
	preferences = {}
	for key, question in questions.items():
		print question
		answer = raw_input().lower() 
		if answer == "y" or answer == "yes":
			print "I'll add it then!"
			preferences[key] = True
		elif answer == "n" or answer == "no":
			print "OK, I'll leave it out!"
			preferences[key] = False
		else:
			print "Try again!"
			
	return preferences
			
# We are creating a make drink method
def make_drink(args):
	drink = []
	for key, value in args.items():
		if value == True:
			ingredient = random.choice(ingredients[key])
			drink.append(ingredient)
	print "Your getting one with" + str(drink) + "!"	
			


print "Welcome to the Pirate Bar! Specializing in spirits of the high seas. What will ye be havin, land lubber?: " 	

# We are calling the make drink method now
def main():
    preferences = your_order()
    drink = make_drink(preferences)
    print "Hope you enjoyed it!"
    answer = raw_input("Would you like another?").lower()
    if answer == "yes" or answer == "y":
    	main()
	print "Sail safely!"


   
  
   
if __name__ == "__main__":
    main()




