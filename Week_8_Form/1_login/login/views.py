from django.shortcuts import render, redirect
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Saving form data to session
            request.session['username'] = form.cleaned_data['username']
            request.session['email'] = form.cleaned_data['email']
            request.session['contact_number'] = form.cleaned_data['contact_number']
            return redirect('success')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def success(request):
    # Retrieving data from session
    username = request.session.get('username', 'User')
    email = request.session.get('email', 'Not provided')
    contact_number = request.session.get('contact_number', 'Not provided')
    return render(request, 'success.html', {
        'username': username,
        'email': email,
        'contact_number': contact_number
    })
