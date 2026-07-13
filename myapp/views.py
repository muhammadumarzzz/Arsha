from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'myapp/index.html')

def portfolio_details(request):
    return render(request, 'myapp/portfolio-details.html')