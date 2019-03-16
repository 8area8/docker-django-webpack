"""Add development datas in the database."""

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Command class."""

    help = 'Add development datas in your database.'

    def handle(self, *args, **options):
        """Handle the command."""
        self.create_superuser()

    def create_superuser(self):
        """Create the superuser."""
        User.objects.create_superuser('admin', 'admin@example.com', 'pass')
