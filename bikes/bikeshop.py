from bikeClasses import *

#Create Bike Shops
bikes2you = BikeShop("Bikes 2 You")
brooklynpeddler = BikeShop("Brooklyn Peddler")
soulcycle = BikeShop("Soul Cycle")


#Create Bikes
mountainbike = Bicycle("Mountain Bike", 400, 350)
babybike = Bicycle("Kid's Bike", 200, 250)
zacbike = Bicycle("Zac bike", 375, 300)
greenbike = Bicycle("Green Bike", 289, 698)
redbike = Bicycle("Red Bike", 106, 999)
goldbike = Bicycle("Golden Bicycle", 700, 12000)

#Create Customers

telemachus = Customer("Telemachus", 500)
dante = Customer("Dante", 300)
figero = Customer("Figero", 693)
jolene = Customer("Jo Jo", 1200)
kimye = Customer("Kimye, yo", 325933)


#Functions
bikes2you.inventory = {babybike: 2, mountainbike:3, zacbike:4, greenbike:1, redbike:3, goldbike:1}

print "Welcome to " + bikes2you.name + "!"
print ""
print bikes2you.list_bikes()
telemachus.can_buy(bikes2you)
print ""
dante.can_buy(bikes2you)
print ""
telemachus.buy_bike(bikes2you, zacbike)
dante.buy_bike(bikes2you, babybike)

print bikes2you.list_bikes()
print bikes2you.show_profit()
print "Telemachus now has " + str(telemachus.budget) + " to spend."
print "Dante now has " + str(dante.budget) + " to spend."
