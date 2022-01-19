from django.shortcuts import render

def GetIceCreams(request):
    return render(request, 'master.html', {'data': {'icecreams':
    [
        {'title': 'Коровка', 'id': 1},
        {'title': 'Магнат', 'id': 2},
        {'title': 'Пингвин', 'id': 3},
    ]
    }})

def GetIceCream(request,id):
    return render(request, 'detail.html', {'data': {
        'id': id,
        'icecream': [
           {'name': '"Коровка"', 'price': '54', 'id': 1},
           {'name': '"Магнат"', 'price': '50', 'id': 2},
           {'name': '"Пингвин"', 'price': '48', 'id': 3},
        ]
    }})
