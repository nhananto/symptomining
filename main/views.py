from django.shortcuts import render

#Home


def home(request):
    return render(request, 'main/home.html')
