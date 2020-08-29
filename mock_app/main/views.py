from django.shortcuts import render


def index(request):
    return render(request,'front/index.html')


def room(request, room_name):
    return render(request, 'front/room.html', {
        'room_name': room_name
    })
