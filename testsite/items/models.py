from django.db import models
from django.contrib.auth.models import User

from stream.models import Stream


class ItemAbstract(models.Model):
    user = models.ForeignKey(User)
    created_at = models.DateTimeField()
    stream = models.OneToOneField(Stream)
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class PhotoItem(ItemAbstract):
    image = models.ImageField()

    def __str__(self):
        return u'Photo %s %s' % (self.id, self.image.url)


class TweetItem(ItemAbstract):
    text = models.CharField(max_length=150)

    def __str__(self):
        return u'Tweet %s %s...' % (self.id, self.text[:10])
