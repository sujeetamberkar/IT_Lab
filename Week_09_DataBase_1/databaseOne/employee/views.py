from django.shortcuts import render, redirect
from .forms import WorksForm, CompanyForm, LivesForm
from .models import Works, Lives

def add_works(request):
    if request.method == 'POST':
        form = WorksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee:add_works')
    else:
        form = WorksForm()
    return render(request, 'employee/add_works.html', {'form': form})

def search_company(request):
    employees = None
    cities = {}
    company_name = ""
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company_name = form.cleaned_data['company_name']
            employees = Works.objects.filter(company_name=company_name)
            for emp in employees:
                try:
                    city = Lives.objects.get(person_name=emp.person_name).city
                    cities[emp.person_name] = city
                except Lives.DoesNotExist:
                    cities[emp.person_name] = "City not found"
            return render(request, 'employee/company_results.html', {'employees': employees, 'cities': cities, 'company_name': company_name})
    else:
        form = CompanyForm()
    return render(request, 'employee/search_company.html', {'form': form})

def add_lives(request):
    if request.method == 'POST':
        form = LivesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee:add_lives')
    else:
        form = LivesForm()
    return render(request, 'employee/add_lives.html', {'form': form})
