from django.conf import settings


class Cart(object):

    def __init__(self, request):
        """Initialization cart"""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)  # get cart from session
        if not cart:  # if no items in cart
            cart = self.session[settings.CART_SESSION_ID] = {}  # get empty cart
        self.cart = cart

    def add(self, product, selected_color, selected_size, quantity=1):
        product_id = product.article + selected_size + selected_color
        if product_id not in self.cart:
            self.cart[product_id] = \
                {'name': product.name,
                 'description': product.description,
                 'article': product.article,
                 'selected_size': selected_size,
                 'selected_color': selected_color,
                 'quantity': quantity,
                 'price': product.price}
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, cart_id):
        if cart_id in self.cart:
            del self.cart[cart_id]
            self.save()

    def __iter__(self):
        cart = self.cart.copy()
        for item in cart.values():
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(item['price']*item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()