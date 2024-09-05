from django.shortcuts import render, redirect, reverse
from django.contrib import messages 

from .forms import OrderForm

# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's notihng in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51PvjOnLlYRI4M6SrSIFOURCUDRvrDNFTMWRCdlkSZcVJIc7YCdK8rtH9LAJIeTwwX0ezEuTIECPT0cQ9HApYNQwf00mEVxkcO6'
    }

    return render(request, template, context)
    