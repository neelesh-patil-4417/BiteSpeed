from django.urls import path
from .views import identify,home

urlpatterns = [
    path('identify/', identify),
    path('', home)
]
