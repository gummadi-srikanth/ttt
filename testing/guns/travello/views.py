from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Destination
def index(request):
    # dest1=Destination()
    # dest1.name='Hyderabad'
    # dest1.desc='it is famous for Biriyani'
    # dest1.img='destination_1_.jpg'
    # dest1.price=700
    # dest2 = Destination()
    # dest2.name = 'Bangalore'
    # dest2.desc = 'its very cool place'
    # dest2.img = 'destination_2_.jpg'
    # dest2.price = 800
    # dest3 = Destination()
    # dest3.name = 'chennaih'
    # dest3.desc = 'it is very hot place '
    # dest3.img = 'destination_3_.jpg'
    # dest3.price = 600
    # dests=[dest1,dest2,dest3]
    dests=Destination.objects.all()

    return render(request,'index.html',{'dests':dests})

# Create your views here.
