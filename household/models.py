from django.db import models
from account.models import Profile

class Family(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Profile, through='Membership')

    class Meta:
        verbose_name_plural = "families"
        db_table = "account_family"

    def __str__(self):
        return self.name

class Membership(models.Model):
    class CommandLevel(models.IntegerChoices):
        MEMBER = 0
        HEAD_HOUSEHOLD = 2

    class Meta:
        db_table = "account_membership"
        ordering = ['-command_level']
        constraints = [
                models.UniqueConstraint(fields=['member', 'family'], name='unique_member')
                ]

    member = models.ForeignKey(Profile, on_delete=models.CASCADE)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    command_level = models.IntegerField(choices=CommandLevel.choices, default=CommandLevel.MEMBER)
