from django.shortcuts import render, redirect
from .forms import InputData

def index(request):
    if request.method == 'POST':
        form = InputData(request.POST)
        if form.is_valid():
            request.session['name']=form.cleaned_data['name']
            request.session['total']=form.cleaned_data['total']
            return redirect ('result')
        
    else:
        form = InputData()
    return render(request,'index.html',{'form':form})

def result(request):
    name = request.session.get('name')
    total=request.session.get('total')
    cgpa=total/50
    params ={'name':name,'cgpa':cgpa}
    return render(request,'result.html',params)


