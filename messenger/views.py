from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django_socketio import broadcast_channel as socketio_broadcast_channel


@csrf_exempt
def broadcast_channel(request, *args, **kwargs):
    """
    API wrapper around ``broadcast_channel`` method of ``django-socketio``.

    """
    channel = request.POST.get('channel')
    message = request.POST.get('message')
    message = '{0}: {1}'.format(channel, message)
    socketio_broadcast_channel(message, channel)
    return HttpResponse
