from django.shortcuts import render
from .models import Hobby, PortfolioItem

def home(request):
    return render(request, 'PortfolioDatabase/home.html', {'message': 'Welcome to my portfolio!', 'summary': 'My name is Brett Asay. I am currently studying web design/development at Weber State University.'})

def hobbies(request):
    hobbies = Hobby.objects.all()
    return render(request, 'PortfolioDatabase/hobbies.html', {'hobbies': hobbies})

def portfolio(request):
    portfolio_items = PortfolioItem.objects.all()
    return render(request, 'PortfolioDatabase/portfolio.html', {'portfolio_items': portfolio_items})

def contact(request):
    email = 'brettasay@mail.weber.edu'
    return render(request, 'PortfolioDatabase/contact.html', {'email': email})
