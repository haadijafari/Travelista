from django.shortcuts import render
from mainPage.forms import ContactForm
from django.contrib import messages

def mainPage(request):
    return render(request, 'Travelista/index.html')

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
