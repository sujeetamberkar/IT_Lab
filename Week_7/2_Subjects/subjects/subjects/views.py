from django.shortcuts import render
from .forms import Data


def firstPage(request):
    form = Data()
    return render(request,"firstPage.html", {'form': form})


def secondPage(request):
    form = Data(request.POST)
    if form.is_valid():
        # Extract the validated data from the form
        subject = form.cleaned_data['subject']
        name = form.cleaned_data['name']
        rollnumber = form.cleaned_data['rollnumber']
        
        # Store data in session
        request.session['subject'] = subject
        request.session['name'] = name
        request.session['rollnumber'] = rollnumber

        # Prepare the context with the form's data
        params = {'subject': subject, 'name': name, 'rollnumber': rollnumber}
        
        # Return a response that renders the secondPage.html template with the context
        return render(request, "secondPage.html", params)
    else:
        # If the form is not valid, re-render the firstPage.html with the form containing error messages
        return render(request, "firstPage.html", {'form': form})
