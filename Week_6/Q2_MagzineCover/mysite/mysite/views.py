from django.shortcuts import render

def index(request):
    cover = None
    if request.method == 'POST':
        selectedImage = request.POST.get('selectedImage')
        backgroundColor = request.POST.get('backgroundColor')
        titleText = request.POST.get('titleText')
        fontSize = request.POST.get('fontSize')
        fontColor = request.POST.get('fontColor')
        
        cover = {
            'selectedImage': f'images/{selectedImage}',
            'backgroundColor': backgroundColor,
            'titleText': titleText,
            'fontSize': fontSize,
            'fontColor': fontColor,
        }
        
    return render(request, "index.html", {'cover': cover})
