from django.db import models
from student.models import Student

class Notes(models.Model):

    c = (('1', '1'), ('2', '2'))



    student  = models.ForeignKey(Student,on_delete = models.CASCADE)


    note1 = models.CharField(max_length=25, choices=c,null=True)
    note2 = models.CharField(max_length=25, choices=c,null=True)
    note3 = models.CharField(max_length=25, choices=c,null=True)
    note4 = models.CharField(max_length=25, choices=c,null=True)
    note5 = models.CharField(max_length=25, choices=c,null=True)
    note6 = models.CharField(max_length=25, choices=c,null=True)
    def __str__(self):
        return str(self.student.student_first_name+" "+self.student.student_last_name)


