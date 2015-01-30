from bikeClasses import *

#Create Bike Shops
bikes2you = BikeShop("Bikes 2 You")
brooklynpeddler = BikeShop("Brooklyn Peddler")
soulcycle = BikeShop("Soul Cycle")


#Create Bikes
mountainbike = Bicycle("Mountain Bike", 400, 350)
babybike = Bicycle("Kid's Bike", 200, 250)
zacbike = Bicycle("Zac Bike", 375, 300)
greenbike = Bicycle("Green Bike", 289, 698)
redbike = Bicycle("Red Bike", 106, 999)
goldbike = Bicycle("Golden Bicycle", 700, 12000)

#Create Customers

telemachus = Customer("Telemachus", 500)
dante = Customer("Dante", 3000)
figero = Customer("Figero", 693)
jolene = Customer("Jo-Jo", 1200)
kimye = Customer("Kimye", 325933)

customers = [telemachus, dante, figero, jolene, kimye]

#Functions
bikes2you.inventory = {babybike: 2, mountainbike:3, zacbike:4, goldbike:1}
brooklynpeddler.inventory = {mountainbike:3, zacbike:4, greenbike:1, redbike:3, goldbike:1}
soulcycle.inventory = {goldbike:100}

#Intro Text
print "Welcome to Bike World! \n\nWe have three great bike stores: {}, {}, and {}. \n".format(brooklynpeddler.name, bikes2you.name, soulcycle.name) 

#Welcome Function
def welcome():
	x = raw_input("Which Bike Store would you like to visit?: (1=bikes2you ; 2=brooklynpeddler; 3=soulcycle)")
	if int(x) == 1:
		bikes2you.list_bikes()
		return bikes2you
	elif int(x) == 2:
		brooklynpeddler.list_bikes()
	elif int(x) == 3:
		soulcycle.list_bikes()
	else:
		print "Sorry, we don't have that store here." 
		welcome()
#Get Customer Name		
def get_name():
	
	raw_name = raw_input("Hey, what's your name?  ('Dante', 'Kimye','Jo-Jo', 'Figero', or 'Telemachus')")
	person = None
	for customer in customers:
		
		if raw_name == customer.name:
			person = customer
		
	if person:
		print "Welcome {}".format(str(person.name)) + "!"
		person.can_buy(shop)
		return person
		pass

	else:
		print "Hey, that's not right!"
		get_name()


#Choose Bike Store
shop = welcome()
customer = get_name()
print "Customer is: " + str(customer.name)
#Show Customers
#telemachus.can_buy(bikes2you)
#jolene.can_buy(brooklynpeddler)
#kimye.can_buy(soulcycle)


#Buy Bikes
#telemachus.buy_bike(bikes2you, zacbike)
dante.buy_bike(bikes2you, babybike)
#kimye.buy_bike(soulcycle, goldbike)

#Show Bike Inventories Again
###bikes2you.list_bikes()

#Show Profit
print bikes2you.show_profit()
#print brooklynpeddler.show_profit()
#print soulcycle.show_profit()

