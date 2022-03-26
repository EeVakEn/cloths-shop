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
        cart_id = product.article + selected_color + selected_size
        if cart_id not in self.cart:
            self.cart[cart_id] = {
                'product_article': product.article,
                'selected_size': selected_size,
                'selected_color': selected_color,
                'quantity': quantity,
            }
        else:
            self.cart[cart_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, cart_id):
        if cart_id in self.cart:
            del self.cart[cart_id]
            self.save()
    #
    # # Перебор всех товаров
    # # Нужно т.к. цена на товары за время сессии может измениться
    # def __iter__(self):
    #     cart = self.cart.copy()
    #     cart_id = self.cart.keys()
    #
    #     for item in cart.values():
    #         item['product'] = Product.objects.get(article__in=item['products']['article'])

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
