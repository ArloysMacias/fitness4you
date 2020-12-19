from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order

@login_required
def profile(request):
    """Display user's profile"""

    if not request.user.is_superuser:
        messages.error(request, "Sorry, you don't seem to have clearance to do that 🤭")
        return redirect(reverse('products'))

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
