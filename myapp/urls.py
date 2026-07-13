from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio_details/', views.portfolio_details, name='portfolio_details'),
]