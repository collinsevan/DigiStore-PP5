from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import UserProfile


@login_required
def profile(request):
    """Profile page."""
    user_profile, _ = UserProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        user_profile.default_full_name = request.POST.get(
            "default_full_name", ""
        )
        user_profile.default_email = request.POST.get("default_email", "")
        user_profile.save()
        messages.success(request, "Profile updated.")

    context = {"profile": user_profile}
    return render(request, "users/profile.html", context)
