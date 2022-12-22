import factory, factory.fuzzy
from factory.django import DjangoModelFactory
from main.models import *



class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    category_name = factory.Faker("word", ext_word_list=['Agricultural', 'Morgage', 'Health', 'Life', 'Travel','Flood'])

class PolicyFactory (DjangoModelFactory):
    class Meta:
        model = Policy
    category = factory.SubFactory(CategoryFactory)
    policy_name = factory.Faker ("word")
    sum_assurance = factory.fuzzy.FuzzyDecimal (low=100, high=5001)
    premium = factory.fuzzy.FuzzyDecimal (low=0, high=4)
    tenure = factory.Faker ("random_number")

class CustomerFactory(DjangoModelFactory):
    class Meta:
        model = Customer
    
    name = factory.Faker("first_name")
    address = factory.Faker("address")
    city = factory.Faker("city")
    country = factory.Faker("country")

class PolicyRecordFactory (DjangoModelFactory):
    class Meta:
        model = PolicyRecord
    customer = factory.SubFactory(CustomerFactory)
    Policy = factory.Iterator(Policy.objects.all())
    status = factory.Faker ("word", ext_word_list=['pending', 'accepted', 'denied'])
    