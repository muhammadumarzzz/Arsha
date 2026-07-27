from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio_details/', views.portfolio_details, name='portfolio_details'),
    path('single/<id>/', views.single_portfolio, name='single'),
    path("subscribe/", views.subscribe, name="subscribe"),
]