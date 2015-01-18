#welcome to the bike shop!

class Bicycle(object):
	def __init__(self, model, weight, production_cost):
		self.model = model
		self.weight = weight
		self.production_cost = production_cost
		#self.markup = 1.2
		#self.finalprice = self.production_cost * self.markup

class BikeShop(object):
	inventory = {}

	def __init__(self, name, inventory):
		self.name = name
		#self.markup = markup
		self.inventory = inventory	

		self.profit = 0
		#need to add a way to list price


	def list_bikes(self):
		print "We have...".format(self.name)
		for b, q in self.inventory.iteritems():
            print "  {} x {}".format(str(q), b.model_name)
		pass

	def sell_bike(self, bike):

		if bike.model in self.inventory:
			print bike.production_cost * 1.2

		else:
			print "Sorry, choose another!"
# don't forget to subtract from inventory
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
	