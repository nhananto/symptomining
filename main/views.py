from django.shortcuts import render

#Home


def home(request):
    return render(request, 'main/index.html')

def checkup(request):
    return render(request, 'main/checkup.html')

def result(request):
    return render(request, 'main/result.html')

def about(request):
    return render(request, 'main/about.html')