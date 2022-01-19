from MyLab2_Django.models import IceCream
from MyLab2_Django.models import Shop
from django.shortcuts import render
from datetime import date

def IceCreamslist(request):
    return render(request, 'icecreams.html', {'data' : {
        'current_date': date.today(),
        'icecreams': IceCream.objects.all() #запрос
    }})

def GetIceCream(request, id):
    ice=IceCream.objects.get(id=id)
    context={
        'id':ice.id,
        'name':ice.name,
        'price':ice.price,
    }
    return render(request, 'icecream.html', context)

def GetShop(request,id):
    sh=Shop.objects.get(pk=id)
    context={
        'icecreamid':sh.icecreamid,
        'name':sh.name,
        'address':sh.address,
    }
    return render(request, 'shop.html', context)

