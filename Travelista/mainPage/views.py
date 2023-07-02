from django.shortcuts import render

def mainPage(request):
    return render(request, 'Travelista/index.html')

def contact(request):
    return render(request, 'Travelista/contact.html')

def about(request):
    return render(request, 'Travelista/about.html')
