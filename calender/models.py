from django.db import models

class AstronomicalEvent(models.Model):
    date = models.DateField(unique=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.date}: {self.description}"