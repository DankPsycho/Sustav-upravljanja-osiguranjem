from django.shortcuts import render
from django.views.generic import ListView
from main.models import Customer, Category , Policy , PolicyRecord




## Create your views here.


def homepage(request):
    return render(request, "index.html")

class CustomerList(ListView):
    model = Customer

class CategoryList(ListView):
    model = Category

class PolicyList(ListView):
    model = Policy

class PolicyRecordList(ListView):
    model = PolicyRecord



