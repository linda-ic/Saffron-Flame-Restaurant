from django.shortcuts import render

def home(request):
    return render(request, 'core/index.html')

def menu(request):
    return render(request, 'core/menu.html')

def reservations(request):
    return render(request, 'core/reservations.html')

def contact(request):
    return render(request, 'core/contact.html')

