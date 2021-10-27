#python manage.py collectstatic

from django.shortcuts import render
from .models import Checkup
import joblib

#Home

def handler404(request, exception):
    return render(request, 'main/error_404.html')

def handler500(request):
    return render(request, 'main/error_404.html')

def home(request):
    return render(request, 'main/home.html')

def checkup(request):
    return render(request, 'main/checkup.html')

def result(request):

    cls = joblib.load('final_model.sav')

    lis= []
    lis.append(request.POST['age'])
    lis.append(request.POST['sex'])
    lis.append(request.POST['fliner'])
    lis.append(request.POST['travel'])
    lis.append(request.POST['crowd'])
    lis.append(request.POST['comorbid'])
    lis.append(request.POST['meet'])
    lis.append(request.POST['fever'])
    lis.append(request.POST['dry_cough'])
    lis.append(request.POST['sore_throat'])
    lis.append(request.POST['diarrhea'])
    lis.append(request.POST['tiredness'])
    lis.append(request.POST['headache'])
    lis.append(request.POST['muscle_pain'])
    lis.append(request.POST['rash_on_skin'])
    lis.append(request.POST['chest_pain'])
    lis.append(request.POST['shortness_breath'])
    lis.append(request.POST['taste_smell'])
    lis.append(request.POST['speech_movement'])
    lis.append(request.POST['saturation'])
    lis.append(request.POST['sentence'])
    lis.append(request.POST['family'])
    #lis.append(request.POST['short_text'])

    print(lis)

    ans = cls.predict([lis])

    print(type(ans))


    if request.method == 'POST':
        if request.POST.get('age') and request.POST.get('sex') and request.POST.get('fliner') and request.POST.get('travel') and request.POST.get('crowd') and request.POST.get('comorbid') and request.POST.get('meet') and request.POST.get('fever') and request.POST.get('dry_cough') and request.POST.get('sore_throat') and request.POST.get('diarrhea') and request.POST.get('tiredness') and request.POST.get('headache') and request.POST.get('muscle_pain') and request.POST.get('rash_on_skin') and request.POST.get('chest_pain') and request.POST.get('shortness_breath') and request.POST.get('taste_smell') and request.POST.get('speech_movement') and request.POST.get('saturation') and request.POST.get('sentence') and request.POST.get('family') and request.POST.get('short_text'):
            checkup = Checkup()
            checkup.age = request.POST.get('age')
            checkup.sex = request.POST.get('sex')
            checkup.fliner = request.POST.get('fliner')
            checkup.travel = request.POST.get('travel')
            checkup.crowd = request.POST.get('crowd')
            checkup.comorbid = request.POST.get('comorbid')
            checkup.meet = request.POST.get('meet')
            checkup.fever = request.POST.get('fever')
            checkup.dry_cough = request.POST.get('dry_cough')
            checkup.sore_throat = request.POST.get('sore_throat')
            checkup.diarrhea = request.POST.get('diarrhea')
            checkup.tiredness = request.POST.get('tiredness')
            checkup.headache = request.POST.get('headache')
            checkup.muscle_pain = request.POST.get('muscle_pain')
            checkup.rash_on_skin = request.POST.get('rash_on_skin')
            checkup.chest_pain = request.POST.get('chest_pain')
            checkup.shortness_breath = request.POST.get('shortness_breath')
            checkup.taste_smell = request.POST.get('taste_smell')
            checkup.speech_movement = request.POST.get('speech_movement')
            checkup.saturation = request.POST.get('saturation')
            checkup.sentence = request.POST.get('sentence')
            checkup.family = request.POST.get('family')
            checkup.short_text = request.POST.get('short_text')
            
            checkup.save()







    return render(request, 'main/result.html',{'ans':ans,'checkup':checkup})

def about(request):
    return render(request, 'main/about.html')

def team(request):
    return render(request, 'main/team.html')
