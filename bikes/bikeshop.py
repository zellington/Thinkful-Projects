from bikescript import *

#Create Bike Shops
bikes2you = BikeShop("Bikes 2 You!")
brooklynpeddler = BikeShop("Brooklyn Peddler")
soulcycle = BikeShop("Soul Cycle")


#Create Bikes
mountainbike = Bicycle("Mountain Bike", 400, 350)
babybike = Bicycle("Kid's Bike", 200, 250)

#Create Customers

bob = Customer("BoB", 5000)

#Functions
bikes2you.inventory = {babybike: 2}

print bikes2you.name
print mountainbike.weight 
print bikes2you.inventory

