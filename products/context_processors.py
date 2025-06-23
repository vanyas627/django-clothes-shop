from contact.models import CartItem

def count_item_cart(request):
    if request.user.is_authenticated:
        cart_item = CartItem.objects.filter(user=request.user, order__isnull=True)
        if cart_item:
            total = len(cart_item)
        else:
            total = 0
    else:
        total = 0

    return {'cart_item': total}