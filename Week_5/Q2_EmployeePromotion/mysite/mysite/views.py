from django.shortcuts import render
from datetime import datetime

def index(request):
    eligibility_result = None
    
    if request.method == 'POST':
        date_of_joining_str = request.POST.get('dateOfJoining')
        date_of_joining = datetime.strptime(date_of_joining_str, '%Y-%m-%d').date()
        years_of_service = datetime.now().date().year - date_of_joining.year

        # Adjust for not yet reached anniversary this year
        if (datetime.now().date().month, datetime.now().date().day) < (date_of_joining.month, date_of_joining.day):
            years_of_service -= 1

        eligibility_result = "YES" if years_of_service >= 5 else "NO"

    return render(request, "index.html", {'eligibility_result': eligibility_result})
