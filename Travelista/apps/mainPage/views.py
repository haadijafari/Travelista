from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm

def mainPage(request):
    return render(request, 'Travelista/index/index.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Your ticket submitted successfully')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Your ticket didn\'t submitted')
    form = ContactForm()
    return render(request, 'Travelista/contact.html', {'form': form})

def about(request):
    return render(request, 'Travelista/about.html')
