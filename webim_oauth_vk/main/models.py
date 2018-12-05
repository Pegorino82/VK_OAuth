from django.db import models
from django.contrib.auth.models import User


class Friend(models.Model):
    friend_id = models.IntegerField()

    first_name = models.CharField(
        max_length=150,
        null=True
    )

    last_name = models.CharField(
        max_length=150,
        null=True
    )

    nickname = models.CharField(
        max_length=150,
        null=True
    )

    photo_50 = models.CharField(
        max_length=500,
        null=True
    )


class Friends(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    friend = models.TextField()
