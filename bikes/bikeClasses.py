#welcome to the bike shop!

class Bicycle(object):
	def __init__(self, model, weight, production_cost):
		self.model = model
		self.weight = weight
		self.production_cost = production_cost
		self.sale_price = production_cost * 1.2
		#self.markup = 1.2
		#self.finalprice = self.production_cost * self.markup
	def __repr__(self):
		return '{}'.format(self.model)

class BikeShop(object):
	def __init__(self, name):
		self.name = name
		self.inventory = {}
		self.profit = 0
		#need to add a way to list price

	def list_bikes(self):
		print "{} currently has in stock:".format(self.name)
		for bike, quantity in self.inventory.iteritems():
			if quantity == 1:
				print "  {} {} for ${}".format(str(quantity), bike.model, bike.sale_price)
			else:
				print "  {} {}s for ${} each".format(str(quantity), bike.model, bike.sale_price)
        print ""

	def sell_bike(self, bike):
		self.inventory[bike] -= 1
		self.profit += bike.production_cost * 0.2

	def show_profit(self):
		return "The profit for {} is ${}.".format(self.name, self.profit)
		print ""
class Customer(object):
	def __init__(self, name, budget):
		self.name = name
		self.budget = budget

	def can_buy(self, shop):
		print self.name + " can buy:"
		for bike, quantity in shop.inventory.iteritems():
			if quantity > 0:
				if (bike.sale_price <= self.budget):
					print bike
				else:
					pass
		print ""
				

	def buy_bike(self, shop, bike):
		self.budget -= bike.sale_price
		print "{} bought a {} for {}".format(self.name, bike.model, bike.sale_price) + " and has ${} left".format(self.budget)
		shop.sell_bike(bike)
		
	