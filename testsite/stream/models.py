from django.db import models
from django.contrib.auth.models import User


class Stream(models.Model):
    user = models.ForeignKey(User)
    created_at = models.DateTimeField()

    def __str__(self):
        return u'Stream %s' % (self.id)
