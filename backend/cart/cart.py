from django.conf import settings

from catalog.models import ProductVariant


class Cart(object):

    def __init__(self, request):
        """Initialization cart"""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)  # get cart from session
        if not cart:  # if no items in cart
            cart = self.session[settings.CART_SESSION_ID] = {}  # get empty cart
        self.cart = cart

    def add(self, product_variant, quantity=1, update_quantity=False):
        product_variant_id = str(product_variant.id)
        if product_variant_id not in self.cart:
            self.cart[product_variant_id] = {
                'quantity': 0,
            }
        if update_quantity:
            self.cart[product_variant_id]['quantity'] = quantity
        else:
            self.cart[product_variant_id]['quantity'] += quantity

        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product_variant):
        if product_variant in self.cart:
            del self.cart[product_variant]
            self.save()

    # Перебор всех товаров
    # Нужно т.к. цена на товары за время сессии может измениться
    def __iter__(self):
        product_variant_ids = self.cart.keys()
        product_variants = ProductVariant.objects.filter(id__in=product_variant_ids)
        cart = self.cart.copy()
        for product_variant in product_variants:
            cart[str(product_variant.id)]['product_variant'] = product_variant

        for item in cart.values():
            item['product_variant'] = ProductVariant.objects.get(article__in=item['products']['article'])

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
