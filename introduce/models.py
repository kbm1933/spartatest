from django.db import models

# Create your models here.
class Admin_AccessLog(models.Model):
    class Meta:
        db_table = "AccessLog"

    location = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)