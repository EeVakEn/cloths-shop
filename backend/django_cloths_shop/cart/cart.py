from django.conf import settings


class Cart(object):

    def __init__(self, request):
        """Initialization cart"""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID) # get cart from session
        if not cart:  # if no items in cart
            cart = self.session[settings.CART_SESSION_ID] = {}  # get empty cart
        self.cart = cart

    def save(self):
        self.session.modified = True

    def add(self, product, selected_size, selected_color, quantity, override_quantity=False):
        product_id = str(product.article)
        if

