from django.db import models

class RSVP(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    attending = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])

    def __str__(self):
        return f"{self.name} - {self.attending}"
