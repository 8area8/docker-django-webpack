"""Home views."""

import logging

from django.views import View
from django.shortcuts import render


class Home(View):
    """Home view."""

    template_name = 'base.html'
    context = {"title": "Home"}
    logger = logging.getLogger('home')

    def get(self, request):
        """Get method for Home view."""
        self.logger.info("IP Address for debug-toolbar: " +
                         request.META['REMOTE_ADDR'])
        return render(request, self.template_name, self.context)
