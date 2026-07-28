from django.shortcuts import render, redirect
from myapp.models import Portfolio, Type, Service, TeamMember, Murojaat, Subscribe
from django.db.models import Q
# Create your views here.

from django.shortcuts import render
from django.db.models import Q
from .models import Portfolio, Type, Service, TeamMember, Murojaat

def home(request):
    if request.method == "POST" and 'subject' in request.POST:
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

    services = Service.objects.filter(is_active=True)
    works = Portfolio.objects.all()
    team_members = TeamMember.objects.filter(is_active=True)

    if request.method == "POST" and 'soz' in request.POST:
        text = str(request.POST.get('soz', '')).strip()
        
        if text:
            services = Service.objects.filter(
                Q(title__icontains=text) | Q(description__icontains=text),
                is_active=True
            )
            
            works = Portfolio.objects.filter(
                Q(nomi__icontains=text) | 
                Q(company_name__icontains=text) |
                Q(date__icontains=text) | 
                Q(url__icontains=text) |
                Q(malumot__icontains=text) | 
                Q(tur__nomi__icontains=text)
            )

            team_members = TeamMember.objects.filter(
                Q(full_name__icontains=text) | 
                Q(position__icontains=text) | 
                Q(bio__icontains=text),
                is_active=True
            )

    context = {
        "portfolios": works,
        "services": services,
        "team_members": team_members,
        "works": works,
        "types": Type.objects.all(),
    }
    
    return render(request, 'myapp/index.html', context)

def filter_index(malumot, id):
    works = Portfolio.objects.filter(tur_id=id)
    turlar = Type.objects.all()
    return render(malumot, 'myapp/index.html', {'works':works, 'types':turlar})

def portfolio_details(request):
    return render(request, 'myapp/portfolio-details.html')

def single_portfolio(malumot, id):
    work = Portfolio.objects.get(id=id)
    return render(malumot, 'myapp/portfolio-details.html', {'work':work})

def subscribe(malumot):
    if malumot.method == "POST":
        email = malumot.POST.get("email")

        Subscribe.objects.create(email=email).save()

    return render(malumot, 'myapp/index.html')