from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('portfolio_details/', views.portfolio_details, name='portfolio_details'),
    path('single/<id>/', views.single_portfolio, name='single'),

]