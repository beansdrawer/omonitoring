from django.db import models

class Record(models.Model) :
    created_at = models.DateTimeField(auto_now_add=True)

    battery = models.CharField(null=True, max_length=20)
    led_color = models.CharField(null=True, max_length=20)
    firmv = models.CharField(null=True, max_length=20)
    encoder = models.CharField(null=True, max_length=20)

    # 걍 추가해봄
    comment = models.TextField(null=True, max_length=300)

    def __str__(self):
        return f'{self.created_at.strftime("%Y/%m/%d %H:%M:%S")}'

    def get_absolute_url(self):
        return f'/monitor/{self.pk}/'