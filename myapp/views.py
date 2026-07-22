from django.shortcuts import render, redirect
from myapp.models import Portfolio, Type, Service, TeamMember, Murojaat
from datetime import datetime
# Create your views here.

def index(request):
    if request.method == "POST":
        ismi = request.POST.get('name')
        mail = request.POST.get('email')
        mavzu = request.POST.get('subject')
        xabar = request.POST.get('message')

        Murojaat.objects.create(
            name=ismi,
            mail=mail,
            title=mavzu,
            text=xabar
        )
        
        return redirect('home')

    works = Portfolio.objects.all()
    turlar = Type.objects.all()
    return render(request, 'myapp/index.html', {'works': works, 'types': turlar})

def filter_index(malumot, id):
    works = Portfolio.objects.filter(tur_id=id)
    turlar = Type.objects.all()
    return render(malumot, 'myapp/index.html', {'works':works, 'types':turlar})

def portfolio_details(request):
    return render(request, 'myapp/portfolio-details.html')

def single_portfolio(malumot, id):
    work = Portfolio.objects.get(id=id)
    return render(malumot, 'myapp/portfolio-details.html', {'work':work})

def home(request):
    portfolios = Portfolio.objects.all()
    services = Service.objects.filter(is_active=True)
    team_members = TeamMember.objects.filter(is_active=True)
    context = {
        "portfolios": portfolios,
        "services": services,
        "team_members": team_members,
    }
    return render(request, "myapp/index.html", context)