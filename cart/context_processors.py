from .cart import Cart


def cart(request):
    """ Конекст-процессор корзины """
    return {'cart': Cart(request)}
