from django.shortcuts import render, redirect
from . forms import SignupForm
from django.contrib import messages

def index(request):
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Registration was successful, you can now login.')

            return redirect('core:login')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
            'form': form
        })

