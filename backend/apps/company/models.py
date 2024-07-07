from django.db import models


class Company(models.Model):
    """
    Компания вакансии
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name