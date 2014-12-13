from bikescript import *

#Create Bike Shops
bikes2you = BikeShop("Bikes 2 You!")
brooklynpeddler = BikeShop("Brooklyn Peddler")
soulcycle = BikeShop("Soul Cycle")


#Create Bikes
mountainbike = Bicycle("Mountain Bike", 400, 350)
babybike = Bicycle("Kid's Bike", 200, 250)
zacbike = Bicycle("A Zac bike!", 375, 300)
greenbike = Bicycle("Green Bike". 289, 698)
redbike = Bicycle("Red Bike", 106, 999)
goldbike = Bicycle("This shit is made of gold!", 700, 12000)

#Create Customers

telemachus = Customer("Telemachus", 5000)
dante = Customer("Dante", 300)
figero = Customer("Figero", 693)
jolene = Customer("Jo Jo", 1200)
kimye = Customer("Kimye, yo", 325933)


#Functions
bikes2you.inventory = {babybike: 2}

print bikes2you.name
print mountainbike.weight 
print bikes2you.inventory

