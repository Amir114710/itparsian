from django.db import models


class Ticket(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField(max_length=3000)

    def __str__(self):
        return self.email
