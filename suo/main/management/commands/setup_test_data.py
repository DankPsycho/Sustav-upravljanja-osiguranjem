import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import Customer , Category , Policy, PolicyRecord
from main.factory import (
    CustomerFactory,
    CategoryFactory,
    PolicyFactory,
    PolicyRecordFactory


)

NUM_CUSTOMER = 15
NUM_POLICY = 4
NUM_CATEGORY = 3
NUM_POLICY_R = NUM_POLICY


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [ Customer , Category , Policy, PolicyRecord ]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        
        

        for _ in range(NUM_CATEGORY):
            category = CategoryFactory()

        for _ in range(NUM_POLICY):
            policy = PolicyFactory()
        
        for _ in range(NUM_CUSTOMER):
            customer = CustomerFactory()

        for _ in range(NUM_POLICY_R):
            policyrecord = PolicyRecordFactory()

        


