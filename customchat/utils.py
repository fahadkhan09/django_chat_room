from channels.db import database_sync_to_async

from .models import ChatRoom


@database_sync_to_async
def get_room_or_error(room_id, user):
    try:
        room = ChatRoom.objects.get(pk=room_id)
    except ChatRoom.DoesNotExist:
        room = None

    return room
