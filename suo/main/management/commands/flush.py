import random

from django.db import transaction
from django.core.management.base import BaseCommand
from main.models import Customer

class Command(BaseCommand):
    help = "Flushes the database"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting data...")
        models = [Customer]
        for m in models:
            m.objects.all().delete()

