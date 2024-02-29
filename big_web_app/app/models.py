from django.db import models


class BetaUser(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    reg_date = models.DateTimeField("date registered")