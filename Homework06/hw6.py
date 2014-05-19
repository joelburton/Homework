"""
  Homework 06

  We found this old script in our git repo and we want to
  improve it.

  Right now, it only tracks a melon's name, if it has seeds and 
  price.  We want add the ability to keep track of flesh color, 
  rind color, average weight.  We also know that our sales team 
  loves to give us additional requirements at the last minute, so
  we want to make it easy on ourselves in the future.

"""

melon_name = {
	1: 'Watermelon',
	2: 'Cantalope'
}

melon_seedless = {
	1: True,
	2: False 
}

melon_price = {
	1: .99,
	2: 1.99
}


def print_melon(name, seedless, price):
	hashasnot = 'have'
	if seedless:
		hashasnot = 'do not have'
	
	print "%ss %s seeds and are $%s" % ( name, hashasnot, price)


print_melon(melon_name[1], melon_seedless[1], melon_price[1])
print_melon(melon_name[2], melon_seedless[2], melon_price[2])
