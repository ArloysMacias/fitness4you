from django.shortcuts import render, get_object_or_404
from .models import UserProfile


def profile(request):
    """Display user's profile"""

    profiles = UserProfile.objects.all()
    print(profiles)

    the_profile = profiles.filter(full_name_default__iexact=request.user)

    print(the_profile)

    template = 'profiles/profile.html'
    context = {
        'profile': the_profile
    }

    return render(request, template, context)
