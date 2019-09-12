from django.shortcuts import render
from .serializers import PaiementSerializer
from .models import paiement
from rest_framework import viewsets
from django.db import connection
import datetime
import random
import string
# Create your views here.
def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
"""def reset():
    a=paiement.objects.all()
    for i in a :
        if  datetime.date.today() == i.valid_until:
            i.paye=False
            i.save()
"""



"""def birthday():
    a=student.objects.all()
    for i in a:
        if datetime.date.today() == i.birthday_date:
            print('happy birthday to {}'.format(i.first_name))"""

#@periodic_task(run_every=crontab(minute=0, hour=0))

def update():     #return to paid=False every valid_until date
    with connection.cursor() as cursor:
        a=randomString(20)
        day=datetime.date.today()
        query="CREATE EVENT {} ON SCHEDULE EVERY 1 MINUTE DO UPDATE paiement_paiement SET paye = False WHERE valid_until = {}".format(a,day)
        
        cursor.execute(query)


class PaiementView(viewsets.ModelViewSet):

    queryset=paiement.objects.all()
    serializer_class=PaiementSerializer

    update()






















"""class update_paiment(UpdateView):




        return Response(serializer.data)


    def update(self,request):
        serializer = PaiementSerializer(many=True)
        new_serializer_data = list(serializer.data)
        new_serializer_data.append({'dict_key': 'dict_value'})
        return Response(new_serializer_data)





    def update(self):
        with connection.cursor() as cursor:
            day=datetime.date.today()
            cursor.execute("UPDATE paiement_paiement SET paye = False WHERE valid_until = %s",[day])"""
