from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name = 'selector-search'),
    path('edit/', views.edit, name = 'selector-edit'),
    path('prefs/', views.prefs, name = 'selector-prefs'),
    path('rec/', views.rec, name = 'selector-rec'),
]