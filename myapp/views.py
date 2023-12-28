from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def team(request):
    return render(request, 'team.html')

def career(request):
    return render(request, 'career.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def contact(request):
    return render(request, 'contact.html')

def hireus(request):
    return render(request, 'hiring.html')