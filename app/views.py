from django.shortcuts import render


def index(request):
    return render(request, 'index.html', locals())

def images(request):
    return render(request, 'images.html', locals())




