from django.shortcuts import render
from myapp.models import Portfolio, Type, Service, TeamMember, Murojaat, Subscribe
# Create your views here.

def home(request):
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
        ).save()

    works = Portfolio.objects.all()
    turlar = Type.objects.all()
    portfolios = Portfolio.objects.all()
    services = Service.objects.filter(is_active=True)
    team_members = TeamMember.objects.filter(is_active=True)
    context = {
            "portfolios": portfolios,
            "services": services,
            "team_members": team_members,
            'works': works, 
            'types': turlar,
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