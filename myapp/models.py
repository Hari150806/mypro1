from django.db import models


class Property(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    type = models.CharField(max_length=10, choices=(('Sale', 'For Sale'), ('Rent', 'For Rent')))
    image = models.URLField()
    description = models.TextField()

    def __str__(self):
        return f"{self.title} ({self.type})"

