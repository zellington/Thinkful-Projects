#welcome to the bike shop!

class Bicycle(object):
	def __init__(self, model, weight, production_cost):
		self.model = model
		self.weight = weight
		self.production_cost = production_cost
		#self.markup = 1.2
		#self.finalprice = self.production_cost * self.markup
	def __repr__(self, model):
		return '{}'.format(str(self.model))

class BikeShop(object):
	def __init__(self, name):
		self.name = name
		self.inventory = {}
		self.profit = 0
		#need to add a way to list price

	def list_bikes(self):
		print "{} currently has in stock:".format(self.name)
		for bike, quantity in self.inventory.iteritems():
            print "  {} x {}".format(str(quantity), bike.model_name)
        print ""

	def sell_bike(self, bike):

		if bike.model in self.inventory:
			self.inventory[bike] -= 1
			self.profit += bike.production_cost * 1.2

		else:
			print "Sorry, choose another!"

	def show_profit(self):
		print "The profit for {} is ${}.".format(self.name, self.profit}

class Customer(object):
	def __init__(self, name, budget):
		self.name = name
		self.budget = budget

	def buy_bike(self, shop, bike):
		self.budget -= bike.production_cost * 1.2
		print "{} bought a {} for {}"
		shop.sell_bike(bike)
		
	