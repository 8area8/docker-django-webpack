"""Home views."""

from django.shortcuts import render


def home(request):
    """Home view."""
    context = {"title": "Home"}
    return render(request, "base.html", context)
