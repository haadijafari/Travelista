from django.shortcuts import render
from django.contrib import messages
from .forms import ContactModelForm

def mainPage(request):
    return render(request, 'Travelista/index/index.html')

def contact(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Your ticket submitted successfully')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Your ticket didn\'t submitted')
    elif request.method == 'GET':
        form = ContactModelForm(initial={'name': 'Anonymous'})
    return render(request, 'Travelista/contact/contact.html', {'form': form})

def about(request):
    return render(request, 'Travelista/about.html')
