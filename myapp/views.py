from django.shortcuts import render
from myapp.models import Portfolio, Type
# Create your views here.

def index(request):
    works = Portfolio.objects.all()
    turlar = Type.objects.all()
    return render(request, 'myapp/index.html', {'works':works, 'types':turlar})

def filter_index(malumot, id):
    works = Portfolio.objects.filter(tur_id=id)
    turlar = Type.objects.all()
    return render(malumot, 'myapp/index.html', {'works':works, 'types':turlar})

def portfolio_details(request):
    return render(request, 'myapp/portfolio-details.html')

def single_portfolio(malumot, id):
    work = Portfolio.objects.get(id=id)
    return render(malumot, 'myapp/portfolio-details.html', {'work':work})