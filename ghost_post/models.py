from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    content = models.CharField(max_length=255)
    is_roast = models.BooleanField()
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now)
    sec_key = models.CharField(max_length=8)

    def __str__(self):
        return self.content

    @property
    def total_votes(self):
        return self.upvote + self.downvote
