from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Tour(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title
    
class BandHistory(models.Model):
    year= models.IntegerField()
    event = models.TextField()
    
    class Meta:
        verbose_name_plural = "Band History"

    def __str__(self):
        return f"{self.year}: {self.event}"

class BandMember(models.Model):
    name = models.CharField(max_length=100)
    instrument = models.CharField(max_length=50)
    year_joined = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

