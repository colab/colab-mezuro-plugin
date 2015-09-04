from django.db import models

class MezuroRepository(models.Model):
    id = models.IntegerField(pk=True)
    name = models.CharField(max_length=255)
    scm_type = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    license = models.CharField(max_length=255)
    period = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    branch = models.CharField(max_length=255)