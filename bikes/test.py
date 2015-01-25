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
dante = Customer("Dante", 300)
figero = Customer("Figero", 693)
jolene = Customer("Jo Jo", 1200)
kimye = Customer("Kimye, yo", 325933)


#Functions
bikes2you.inventory = {babybike: 2, mountainbike:3, zacbike:4, goldbike:1}
brooklynpeddler.inventory = {mountainbike:3, zacbike:4, greenbike:1, redbike:3, goldbike:1}
soulcycle.inventory = {goldbike:100}

#Intro Text
print "Welcome to Bike World! \n\nWe have three great bike stores: {}, {}, and {} ".format(brooklynpeddler.name, bikes2you.name, soulcycle.name) 
#Show Bike Store Inventories
bikes2you.list_bikes()
brooklynpeddler.list_bikes()
soulcycle.list_bikes()
#Show Customers
telemachus.can_buy(bikes2you)
jolene.can_buy(brooklynpeddler)
kimye.can_buy(soulcycle)
dante.can_buy(bikes2you)

#Buy Bikes
telemachus.buy_bike(bikes2you, zacbike)
dante.buy_bike(bikes2you, babybike)
kimye.buy_bike(soulcycle, goldbike)
#Show Bike Inventories Again
###bikes2you.list_bikes()
#Show Profit
print bikes2you.show_profit()
print brooklynpeddler.show_profit()
print soulcycle.show_profit()
