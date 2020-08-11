from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from customchat.models import ChatRoom


def CreateChatRoom(request):
    # Get a list of rooms, ordered alphabetically
    rooms = ChatRoom.objects.create(owner=request.user)
    return HttpResponseRedirect('chat_room/' + str(rooms.id))


def CustomChatRoom(request, slug):
    if not request.user.is_anonymous:
        try:
            room = ChatRoom.objects.filter(id=slug)
        except:
            room = None
        message = {'status': 'active'}
        if len(room) > 0:
            message['rooms'] = room
            message['room_id'] = room.first().id

        else:
            message = {'status': 'inactive'}

        return render(request, "chat_room.html", message)

    else:
        return redirect('/login/')


def index(request):
    return render(request, "index.html")
