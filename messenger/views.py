from django.http import HttpResponse

from django_socketio import broadcast_channel as socketio_broadcast_channel


def broadcast_channel(request, *args, **kwargs):
    channel = request.POST.get('channel')
    message = request.POST.get('message')
    socketio_broadcast_channel(message, channel)
    return HttpResponse
