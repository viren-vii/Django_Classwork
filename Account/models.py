from django.db import models

class Acc_information(models.Model):
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    email = models.EmailField()
    date = models.DateField()
    status = models.BooleanField()



