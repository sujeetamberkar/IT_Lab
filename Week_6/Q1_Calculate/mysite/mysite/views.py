from django.shortcuts import render

def index(request):
    result = None
    if request.method == 'POST':
        number1 = int(request.POST.get('number1'))
        number2 = int(request.POST.get('number2'))
        operation = request.POST.get('operation')

        if operation == 'add':
            result = number1 + number2
        elif operation == 'subtract':
            result = number1 - number2
        elif operation == 'multiply':
            result = number1 * number2
        elif operation == 'divide':
            if number2 != 0:
                result = number1 / number2
            else:
                result = 'Cannot divide by zero'
        else:
            result = 'Invalid operation'

    return render(request, "index.html", {'result': result})
