from django.shortcuts import render
from .models import Destination
def index(request):
    desti1 = Destination()
    desti1.img = 'destination_1.jpg'
    desti1.location = 'Bombay'
    desti1.price = 789
    desti1.desc = 'The city that never sleeps, Dream city of India'
    desti1.offer = False

    desti2 = Destination()
    desti2.img = 'destination_2.jpg'
    desti2.location = 'Delhi'
    desti2.price = 543
    desti2.desc = 'The National Capital Territory (NCT) of Delhi, Heart of India'
    desti2.offer = False

    desti3 = Destination()
    desti3.img = 'destination_3.jpg'
    desti3.location = 'Indore'
    desti3.price = 421
    desti3.desc = 'Food, forts and festivals - Indore rocks it all!'
    desti3.offer = True

    destis = [desti1,desti2,desti3]
    return render(request,"index.html", {'destis':destis})
