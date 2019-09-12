from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    c = (('temps complet', 'Temp Complet'), ('temps partiel', 'Temps Partiel'))
    group_choices = (('petit-section', 'Petit-Section'), ('moyenne-section', 'Moyenne-Section'), ('grand-section', 'Grand-Section'))
    # coté parent
    parent = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    student_first_name = models.CharField(max_length=20)
    student_last_name = models.CharField(max_length=20)
    student_sexe = models.CharField(max_length=25)
    nationality = models.CharField(max_length=20)
    student_birthday = models.CharField(max_length=20)
    father_name = models.CharField(max_length=25)
    father_profession = models.CharField(max_length=25)
    father_phone_number = models.CharField(max_length=25)
    mother_name = models.CharField(max_length=20)
    mother_profession = models.CharField(max_length=25)
    mother_phone_number = models.CharField(max_length=25)
    complete_adress = models.CharField(max_length=100)
    tlf_fix_number = models.CharField(max_length=30)
    img = models.ImageField(upload_to='images/', default="/images/profile-2398782_960_720_ZjcWbXL.png")

    # coté admin

    section = models.CharField(max_length=25, choices=group_choices)
    nom_du_pediatre = models.CharField(max_length=25)
    tlf_pediatre = models.CharField(max_length=25)
    other_responsible_name = models.CharField(max_length=25)
    other_responsible_ltf = models.CharField(max_length=25)
    is_alergetic = models.BooleanField(default=False)
    whos_alergetic = models.CharField(max_length=25)
    auto_medic_buy = models.BooleanField(default=True)
    study_forfait = models.CharField(max_length=25, choices=c)
    def __str__(self):
        return self.student_first_name+" "+self.student_last_name