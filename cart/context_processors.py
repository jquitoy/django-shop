from .cart import Cart

# create context processor so our cart can work on all pages of site

def cart(request):
	# return default data from cart
	return {'cart': Cart(request)}