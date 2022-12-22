from django.contrib import admin
from main.models import *

models_list = [ Customer, Category, Policy, PolicyRecord]

admin.site.register(models_list)