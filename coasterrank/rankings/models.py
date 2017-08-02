from django.db import models
from coasterrank.coasters.models import RollerCoaster


class HeadToHead():
    """Direct head to head match-up between two roller coasters"""
    creation_date = models.DateField(auto_now=True)
