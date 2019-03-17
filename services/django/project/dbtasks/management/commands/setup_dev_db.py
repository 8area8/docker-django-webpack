"""Add development datas in the database."""

import logging

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError


class Command(BaseCommand):
    """Command class."""

    help = 'Add development datas in your database.'

    def handle(self, *args, **options):
        """Handle the command."""
        self.create_superuser()

    def create_superuser(self):
        """Create the superuser."""
        logger = logging.getLogger('base')
        admin_context = ('admin', 'admin@example.com', 'pass')
        try:
            User.objects.create_superuser(*admin_context)
        except IntegrityError:
            logger.warning("'admin' user already exists.")
