from django.shortcuts import render
from .forms import CarForm

def index(request):
    form = CarForm()
    return render(request, "index.html", {'form': form})

def details(request):
    form = CarForm(request.POST)
    if form.is_valid():
        model = form.cleaned_data['cars']
        text = form.cleaned_data['text']
        print(text)
        print(model)
        params = {'model': model, 'text': text}
        return render(request, 'details.html', params)
    else:
        # In case the form is not valid, redirect back to index or handle accordingly
        return render(request, "index.html", {'form': form})
