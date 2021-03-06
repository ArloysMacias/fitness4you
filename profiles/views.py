from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


@login_required
def profile(request):
    """Display user's profile"""

    the_profile = get_object_or_404(UserProfile, user=request.user)

    orders = the_profile.orders.all()
    template = 'profiles/profile.html'
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=the_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile have been successfully updated')
        else:
            messages.error(request, 'ERROR | Update failed. Please check the form')
    else:
        form = UserProfileForm(instance=the_profile)

    context = {
        'form': form,
        'orders': orders,
        'fromprofile': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
