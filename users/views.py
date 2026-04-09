from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)
from django.urls import reverse

from checkout.models import Order
from .forms import ProductSuggestionForm, UserProfileForm
from .models import ProductSuggestion, UserProfile


@login_required
def profile(request):
    """Display and update the logged-in user's profile."""
    user_profile, _ = UserProfile.objects.get_or_create(user=request.user)
    orders = user_profile.orders.all()
    suggestions = request.user.product_suggestions.all()

    if request.method == "POST":
        if "update_profile" in request.POST:
            form = UserProfileForm(
                request.POST,
                instance=user_profile,
            )
            suggestion_form = ProductSuggestionForm()

            if form.is_valid():
                form.save()
                messages.success(request, "Profile updated.")
                return redirect(reverse("profile"))

            messages.error(
                request,
                "Update failed. Please check the form and try again."
            )

        elif "add_suggestion" in request.POST:
            form = UserProfileForm(instance=user_profile)
            suggestion_form = ProductSuggestionForm(request.POST)

            if suggestion_form.is_valid():
                suggestion = suggestion_form.save(commit=False)
                suggestion.user = request.user
                suggestion.save()
                messages.success(
                    request,
                    "Product suggestion submitted successfully."
                )
                return redirect(reverse("profile"))

            messages.error(
                request,
                (
                    "Failed to submit product suggestion. "
                    "Please check the form and try again."
                ),
            )

        else:
            form = UserProfileForm(instance=user_profile)
            suggestion_form = ProductSuggestionForm()

    else:
        form = UserProfileForm(instance=user_profile)
        suggestion_form = ProductSuggestionForm()

    context = {
        "form": form,
        "orders": orders,
        "suggestions": suggestions,
        "suggestion_form": suggestion_form,
        "on_profile_page": True,
    }
    return render(request, "users/profile.html", context)


@login_required
def edit_product_suggestion(request, suggestion_id):
    """Allow a user to edit their own product suggestion."""
    suggestion = get_object_or_404(
        ProductSuggestion,
        pk=suggestion_id,
        user=request.user,
    )

    if request.method == "POST":
        form = ProductSuggestionForm(
            request.POST,
            instance=suggestion,
        )

        if form.is_valid():
            updated_suggestion = form.save(commit=False)
            updated_suggestion.status = ProductSuggestion.STATUS_PENDING
            updated_suggestion.admin_notes = ""
            updated_suggestion.save()
            messages.success(
                request,
                "Product suggestion updated successfully."
            )
            return redirect(reverse("profile"))

        messages.error(
            request,
            (
                "Failed to update product suggestion. "
                "Please check the form and try again."
            ),
        )

    else:
        form = ProductSuggestionForm(instance=suggestion)
        messages.info(
            request,
            f"You are editing your suggestion for {suggestion.suggested_name}."
        )

    context = {
        "suggestion": suggestion,
        "form": form,
    }
    return render(request, "users/edit_product_suggestion.html", context)


@login_required
def delete_product_suggestion(request, suggestion_id):
    """Allow a user to delete their own product suggestion."""
    suggestion = get_object_or_404(
        ProductSuggestion,
        pk=suggestion_id,
        user=request.user,
    )

    if request.method == "POST":
        suggestion.delete()
        messages.success(
            request,
            "Product suggestion deleted successfully."
        )
        return redirect(reverse("profile"))

    context = {
        "suggestion": suggestion,
    }
    return render(
        request,
        "users/delete_product_suggestion.html",
        context,
    )


@login_required
def order_history(request, reference):
    """Display a past order confirmation from the user's profile."""
    user_profile, _ = UserProfile.objects.get_or_create(user=request.user)

    order = get_object_or_404(
        Order,
        reference=reference,
        user_profile=user_profile,
    )

    messages.info(
        request,
        (
            f"This is a past confirmation for order {reference}. "
            "A confirmation email was sent on the order date."
        ),
    )

    context = {
        "order": order,
        "from_profile": True,
    }

    return render(
        request,
        "checkout/checkout_success.html",
        context,
    )
