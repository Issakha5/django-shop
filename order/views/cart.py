from django.conf import settings
from django.shortcuts import render

from order.cart import Cart

from product.models.product import Product


def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return render(request, 'order/partials/menu_cart.html', {'cart': cart})


def cart(request):
    return render(request, 'order/cart.html')


def success(request):
    return render(request, 'order/success.html')


def update_cart(request, product_id, action):
    cart = Cart(request)

    if action == 'increment':
        cart.add(product_id, 1, True)
    else:
        cart.add(product_id, -1, True)

    product = Product.objects.get(pk=product_id)
    quantity = cart.get_item(product_id)

    if quantity:
        quantity = quantity['quantity']

        item = {
            'product': {
                'id': product.id,
                'name': product.name,
                'image': product.image,
                'get_thumbnail': product.get_thumbnail(),
                'price': product.price,
            },
            'total_price': (quantity * product.price) / 100,
            'quantity': quantity,
        }
    else:
        item = None

    response = render(request, 'order/partials/cart_item.html', {'item': item})
    response['HX-Trigger'] = 'update-menu-cart'

    return response


#@login_required
def checkout(request):
    pub_key = settings.STRIPE_API_KEY_PUBLISHABLE
    return render(request, 'order/checkout.html', {'pub_key': pub_key})


def hx_menu_cart(request):
    return render(request, 'order/partials/menu_cart.html')


def hx_cart_total(request):
    return render(request, 'order/partials/cart_total.html')
