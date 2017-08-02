from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):

    user = models.OneToOneField(User)
    name = models.CharField(max_length=100, blank=True, null=True)
    ridden_coasters = models.ManyToManyField('coasters.RollerCoaster', related_name='riders')

    def __repr__(self):
        return '<UserProfile %s>' % (self.user.username,)

    def __str__(self):
        return self.user.username
