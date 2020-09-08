import uuid

from django.db import models
from django.contrib.auth.models import User


class ChatRoom(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, )

    def __str__(self):
        return 'RoomId-' + str(self.id)

    @property
    def group_name(self):
        return "room-%s" % self.id
