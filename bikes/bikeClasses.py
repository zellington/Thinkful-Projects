#welcome to the bike shop!

class Bicycle(object):
	def __init__(self, model, weight, production_cost):
		self.model = model
		self.weight = weight
		self.production_cost = production_cost
		self.markup = 1.2
		self.finalprice = self.production_cost * self.markup
		pass

class BikeShop(object):
	def __init__(self, name):
		self.name = name
		self.inventory = {}
		self.profit = 0

	def list_bikes(self):
		print "We have...".format(self.name)
		pass

class Customer(object):
	def __init__(self, name, budget):
		self.name = name
		self.budget = budget

	def greeting(self, name):
		print "%s wants to buy a bike!" % name

		pass

	def buy_bike(self, shop, bike):
		pass
	