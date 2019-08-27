from django.db import models


class HandBook(models.Model):
    # Телефонный справочник
    full_name = models.CharField(max_length=70)
    number = models.CharField(max_length=20)
    description = models.TextField()

    class Meta:
        verbose_name = "Phone HandBook"

    #def __str__(self):              # __unicode__ on Python 2
    #    return "name: "+self.full_name+", number: " + self.number
