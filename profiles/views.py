from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """Display user's profile"""
    the_profile = get_object_or_404(UserProfile, user=request.user)

    print(the_profile)

    form = UserProfileForm(instance=the_profile)
    orders = the_profile.orders.all()
    template = 'profiles/profile.html'
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=the_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile have been successfully updated')
    context = {
        'form': form,
        'orders': orders,
        'fromprofile': True
    }

    return render(request, template, context)
