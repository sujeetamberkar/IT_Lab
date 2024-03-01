from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # pass
    # Initialize variables to None for conditional checks in the template
    details = None
    totalPercentage = None
    
    if request.method == 'POST':
        # Extracting form data
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        english = int(request.POST.get('english'))
        physics = int(request.POST.get('physics'))
        chemistry = int(request.POST.get('chemistry'))

        # Calculating total percentage
        total_marks = english + physics + chemistry
        percentage = (total_marks / 300) * 100

        # Preparing the string to display in the template
        details = (f"Name: {name}\nDOB: {dob}\nAddress: {address}\n"
                   f"Contact: {contact}\nEmail: {email}\n"
                   f"English: {english}\nPhysics: {physics}\n"
                   f"Chemistry: {chemistry}\n"
                   f"Percentage: {percentage:.2f}%\n\n")

        totalPercentage = f"Total Percentage: {percentage:.2f}%"

    # Render the same template for GET (initial form) and POST (form submission) requests
    return render(request, "index.html", {
        'details': details,
        'totalPercentage': totalPercentage
    })
