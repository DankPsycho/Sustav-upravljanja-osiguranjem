from django.urls import path 
from . import views

from main.views import CustomerList , CategoryList , PolicyList , PolicyRecordList


app_name = 'main'  # here for namespacing of urls.

urlpatterns = [

    path('', views.homepage, name='index'),
    path('customers/', CustomerList.as_view()), 
    path('category/', CategoryList.as_view()),
    path('policyrecord/', PolicyRecordList.as_view()),
    path('policy/', PolicyList.as_view())
    
    
]
