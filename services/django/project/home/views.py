"""Home views."""

from django.views import View
from django.shortcuts import render


class Home(View):
    """Home view."""

    template_name = 'base.html'
    context = {"title": "Home"}

    def get(self, request):
        """Get method for Home view."""
        return render(request, self.template_name, self.context)
