from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'

class Family(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Profile, through='Membership')

    class Meta:
        verbose_name_plural = "families"

    def __str__(self):
        return self.name

class Membership(models.Model):
    class CommandLevel(models.IntegerChoices):
        MEMBER = 0
        HEAD_HOUSEHOLD = 2

    member = models.OneToOneField(Profile, on_delete=models.CASCADE)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    command_level = models.IntegerField(choices=CommandLevel.choices, default=CommandLevel.MEMBER)
