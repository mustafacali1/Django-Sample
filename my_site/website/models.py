from django.db import models
from datetime import time


class Room(models.Model):
    name = models.CharField(max_length=50, unique=True)
    floor = models.CharField(max_length=50)
    room_number = models.IntegerField(default=101)

    class Meta:
        verbose_name_plural = 'rooms'

    def __str__(self):
        return (f'{self.name}: room '
                f'{self.room_number} on floor '
                f'{self.floor}')


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return (f'{self.title} at '
                f'{self.start_time} on '
                f'{self.date}')

    class Meta:
        verbose_name_plural = 'meetings'









