from django.db import models

class Record(models.Model) :
    created_at = models.DateTimeField(auto_now_add=True)

    battery = models.CharField(max_length=20)
    led_color = models.CharField(max_length=20)

    def __str__(self):
        return f'[{self.pk}]{self.created_at} log'