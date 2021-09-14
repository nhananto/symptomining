from django.shortcuts import render

#Home


def home(request):
    return render(request, 'main/index.html')

def checkup(request):
    return render(request, 'main/checkup.html')