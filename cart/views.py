from django.shortcuts import render

# Create your views here.

def view_cart(request):
    """ A view renders the shopping cart contents page """

    return render(request, 'cart/cart.html')