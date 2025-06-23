from django.shortcuts import render,redirect, get_object_or_404
from .forms import ContactForm, OrderForm
from .models import Order, CartItem
from products.models import Products
from django.contrib.auth.decorators import login_required
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ContactForm()

    return render(request, 'contact.html', context={'form':form})



@login_required
def cart_view(request):
    if request.method == 'POST':
        product_id = request.POST.get('product-id')
        size = request.POST.get('product-size')
        quantity = int(request.POST.get('product-quanity'))
        color = request.POST.get('product-color')
        product = Products.objects.get(id=product_id)

        cart_item = CartItem(user= request.user, product=product, size=size, quantity=quantity, price=product.price, color=color)
        cart_item.save()
        all_cart = CartItem.objects.filter(user=request.user, order__isnull=True)
        all_sum = sum(item.total() for item in CartItem.objects.filter(user=request.user, order__isnull=True))
        return render(request, 'order.html', context={'order': all_cart,
                                                  'total': cart_item.total(),
                                                  'all_sum': all_sum})
    else:
        all_cart = CartItem.objects.filter(user=request.user, order__isnull=True)
        all_sum = sum(item.total() for item in CartItem.objects.filter(user=request.user, order__isnull=True))
        return render(request, 'order.html', context={'order': all_cart,
                                                  'all_sum': all_sum})


def delete_item_in_cart(request, item_id):

    if request.method == 'POST':
        item = get_object_or_404(CartItem, id=item_id, user=request.user)
        item.delete()
    return redirect('/order/')


@login_required
def checkout_view(request):
    if request.method == 'POST':
        cart_items = CartItem.objects.filter(user=request.user, order__isnull=True)
        form = OrderForm(request.POST)

        if form.is_valid():
            order = form.save()
            order.user = request.user
            order.save()

            for item in cart_items:
                item.order = order
                item.save()

            return redirect('/')
        else:
            return render(request, 'cart.html', context={'form': form})
    else:
        form = OrderForm()
        return render(request, 'cart.html', context={'form': form})


def history_orders_views(request):
    cart_items = CartItem.objects.filter(user=request.user, order__isnull=False)
    order_dict = {}
    total = 0

    for item in cart_items:
        order = item.order
        if order not in order_dict:
            order_dict[order] = {'items': [],
                                 'total': 0}
        order_dict[order]['items'].append(item)
        order_dict[order]['total'] += item.total()


    return render(request, 'orders_history.html', context={'orders_dict': order_dict,
                                                                        'order_items': cart_items,
                                                                        'total': total})
