from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import UserProfileForm
from .models import UserProfile


@login_required
def profile(request):
    """Display and update the logged-in user's profile."""
    user_profile, _ = UserProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
        else:
            messages.error(
                request,
                "Update failed. Please check the form and try again."
            )
    else:
        form = UserProfileForm(instance=user_profile)

    context = {
        "form": form,
        "profile": user_profile,
    }
    return render(request, "users/profile.html", context)
