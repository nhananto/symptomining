from django.db import models

# Create your models here.


class Checkup(models.Model):
    age = models.IntegerField()
    sex=models.CharField(max_length=10)
    fliner = models.CharField(max_length=5)
    travel = models.CharField(max_length=5)
    crowd = models.CharField(max_length=5)
    comorbid = models.CharField(max_length=5)
    meet = models.CharField(max_length=5)
    fever = models.CharField(max_length=200)
    dry_cough = models.CharField(max_length=200)
    sore_throat = models.CharField(max_length=200)
    diarrhea = models.CharField(max_length=200)
    tiredness = models.CharField(max_length=200)
    headache = models.CharField(max_length=200)
    muscle_pain = models.CharField(max_length=200)
    rash_on_skin = models.CharField(max_length=200)
    chest_pain = models.CharField(max_length=200)
    shortness_breath = models.CharField(max_length=200)
    taste_smell = models.CharField(max_length=200)
    speech_movement = models.CharField(max_length=200)
    saturation = models.CharField(max_length=200)
    sentence = models.CharField(max_length=10)
    family = models.CharField(max_length=10)
    short_text = models.TextField(max_length=1000, blank=True, null=True, default=False)





