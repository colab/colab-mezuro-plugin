from django.db import models
from django.utils.translation import ugettext_lazy as _

class MezuroRepository(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    scm_type = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    license = models.CharField(max_length=255)
    period = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    branch = models.CharField(max_length=255)

    class Meta:
        verbose_name = _('Mezuro Repository')
        verbose_name_plural = _('Mezuro Repositories')