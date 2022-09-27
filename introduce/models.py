from django.db import models

# Create your models here.
class Admin_AccessLog(models.Model):
    location = models.CharField("접속 경로",max_length=256)
    created_at = models.DateTimeField("접속 시간",auto_now_add=True)

    def __str__(self):
        return f"{self.created_at} / {self.location}"