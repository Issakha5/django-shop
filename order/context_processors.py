from order.models.cart import Cart


def cart(request):
    return {"cart": Cart(request)}
