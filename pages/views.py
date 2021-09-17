from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'pages/about.html')


def service(request):
    return render(request, 'pages/service.html')


def why_us(request):
    return render(request, 'pages/why_us.html')
