from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name = 'selector-search'),
    path('edit/', views.edit, name = 'selector-edit'),
]