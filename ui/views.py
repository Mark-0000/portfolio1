from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ContactForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Thank you for contacting me. I be will in touch with you soon!')
        else:
            messages.success(request, f'Sorry, your form was invalid. Please try again!')
        return redirect(reverse('ui-home') + '#contact')
    else:
        form = ContactForm(request.POST)
    context = {
        'projects': Project.objects.all(),
        'form': form
    }
    return render(request, 'ui/index.html', context)

