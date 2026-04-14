from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import modelform_factory
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)
from django.urls import reverse

from checkout.models import Order
from .forms import ProductSuggestionForm, UserProfileForm
from .models import (
    ProductSuggestion,
    SavedSearch,
    SupportTicket,
    UserProfile,
)


SavedSearchForm = modelform_factory(
    SavedSearch,
    fields=(
        "title",
        "query",
    ),
)

SupportTicketForm = modelform_factory(
    SupportTicket,
    fields=(
        "subject",
        "message",
    ),
)


@login_required
def profile(request):
    """Display and update the logged-in user's profile."""
    user_profile, _ = UserProfile.objects.get_or_create(user=request.user)
    orders = user_profile.orders.all()
    suggestions = request.user.product_suggestions.all()
    saved_searches = request.user.saved_searches.all()
    support_tickets = request.user.support_tickets.all()

    if request.method == "POST":
        if "update_profile" in request.POST:
            form = UserProfileForm(
                request.POST,
                instance=user_profile,
            )
            suggestion_form = ProductSuggestionForm()
            saved_search_form = SavedSearchForm()
            support_ticket_form = SupportTicketForm()

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
            saved_search_form = SavedSearchForm()
            support_ticket_form = SupportTicketForm()

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

        elif "add_saved_search" in request.POST:
            form = UserProfileForm(instance=user_profile)
            suggestion_form = ProductSuggestionForm()
            saved_search_form = SavedSearchForm(request.POST)
            support_ticket_form = SupportTicketForm()

            if saved_search_form.is_valid():
                saved_search = saved_search_form.save(commit=False)
                saved_search.user = request.user
                saved_search.save()
                messages.success(
                    request,
                    "Saved search added successfully."
                )
                return redirect(reverse("profile"))

            messages.error(
                request,
                (
                    "Failed to save search. "
                    "Please check the form and try again."
                ),
            )

        elif "add_support_ticket" in request.POST:
            form = UserProfileForm(instance=user_profile)
            suggestion_form = ProductSuggestionForm()
            saved_search_form = SavedSearchForm()
            support_ticket_form = SupportTicketForm(request.POST)

            if support_ticket_form.is_valid():
                support_ticket = support_ticket_form.save(commit=False)
                support_ticket.user = request.user
                support_ticket.save()
                messages.success(
                    request,
                    "Support ticket submitted successfully."
                )
                return redirect(reverse("profile"))

            messages.error(
                request,
                (
                    "Failed to submit support ticket. "
                    "Please check the form and try again."
                ),
            )

        else:
            form = UserProfileForm(instance=user_profile)
            suggestion_form = ProductSuggestionForm()
            saved_search_form = SavedSearchForm()
            support_ticket_form = SupportTicketForm()

    else:
        form = UserProfileForm(instance=user_profile)
        suggestion_form = ProductSuggestionForm()
        saved_search_form = SavedSearchForm()
        support_ticket_form = SupportTicketForm()

    context = {
        "form": form,
        "orders": orders,
        "suggestions": suggestions,
        "suggestion_form": suggestion_form,
        "saved_searches": saved_searches,
        "saved_search_form": saved_search_form,
        "support_tickets": support_tickets,
        "support_ticket_form": support_ticket_form,
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
def edit_saved_search(request, saved_search_id):
    """Allow a user to edit their own saved search."""
    saved_search = get_object_or_404(
        SavedSearch,
        pk=saved_search_id,
        user=request.user,
    )

    if request.method == "POST":
        form = SavedSearchForm(
            request.POST,
            instance=saved_search,
        )

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Saved search updated successfully."
            )
            return redirect(reverse("profile"))

        messages.error(
            request,
            (
                "Failed to update saved search. "
                "Please check the form and try again."
            ),
        )

    else:
        form = SavedSearchForm(instance=saved_search)
        messages.info(
            request,
            f"You are editing saved search {saved_search.title}."
        )

    context = {
        "saved_search": saved_search,
        "form": form,
    }
    return render(request, "users/edit_saved_search.html", context)


@login_required
def delete_saved_search(request, saved_search_id):
    """Allow a user to delete their own saved search."""
    saved_search = get_object_or_404(
        SavedSearch,
        pk=saved_search_id,
        user=request.user,
    )

    if request.method == "POST":
        saved_search.delete()
        messages.success(
            request,
            "Saved search deleted successfully."
        )
        return redirect(reverse("profile"))

    context = {
        "saved_search": saved_search,
    }
    return render(
        request,
        "users/delete_saved_search.html",
        context,
    )


@login_required
def edit_support_ticket(request, ticket_id):
    """Allow a user to edit their own support ticket."""
    support_ticket = get_object_or_404(
        SupportTicket,
        pk=ticket_id,
        user=request.user,
    )

    if request.method == "POST":
        form = SupportTicketForm(
            request.POST,
            instance=support_ticket,
        )

        if form.is_valid():
            updated_ticket = form.save(commit=False)
            updated_ticket.status = SupportTicket.STATUS_OPEN
            updated_ticket.save()
            messages.success(
                request,
                "Support ticket updated successfully."
            )
            return redirect(reverse("profile"))

        messages.error(
            request,
            (
                "Failed to update support ticket. "
                "Please check the form and try again."
            ),
        )

    else:
        form = SupportTicketForm(instance=support_ticket)
        messages.info(
            request,
            f"You are editing support ticket {support_ticket.subject}."
        )

    context = {
        "support_ticket": support_ticket,
        "form": form,
    }
    return render(request, "users/edit_support_ticket.html", context)


@login_required
def delete_support_ticket(request, ticket_id):
    """Allow a user to delete their own support ticket."""
    support_ticket = get_object_or_404(
        SupportTicket,
        pk=ticket_id,
        user=request.user,
    )

    if request.method == "POST":
        support_ticket.delete()
        messages.success(
            request,
            "Support ticket deleted successfully."
        )
        return redirect(reverse("profile"))

    context = {
        "support_ticket": support_ticket,
    }
    return render(
        request,
        "users/delete_support_ticket.html",
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
