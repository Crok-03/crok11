from django.db import models


class Record(models.Model):
    name = models.CharField(max_length=49)
    date = models.DateTimeField()

    def __str__(self):
        return self.name