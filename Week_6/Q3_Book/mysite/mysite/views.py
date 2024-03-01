from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def metadata(request):
    return render(request, "meta.html")

def reviews(request):
    return render(request, "reviews.html")

def publisher_info(request):
    return render(request, "publisher.html")
