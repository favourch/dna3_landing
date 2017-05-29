from __future__ import unicode_literals

from django.db import models

# Create your models here.


class MailList(models.Model):
    email = models.EmailField()

    def __unicode__(self):
        return self.email

    def __str__(self):
        return self.email

