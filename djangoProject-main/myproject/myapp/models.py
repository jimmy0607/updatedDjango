from django.db import models

# Create your models here.
class Album(models.Model):
    """
    A model class representing an album.
    Attributes:
    title (str): The title of the album.
    release_date (date): The date the album was released.
    description (str): A brief description of the album.

    Methods:
    __str__(): Returns the title of the album as a string.
    """
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        """
        Return a string representation of the album object.
        """
        return self.title
    
class Tour(models.Model):
    """
    A class representing a music tour.

    Attributes:
        title (str): The title of the tour.
        location (str): The location of the tour.
        date (date): The date of the tour.
        description (str): A description of the tour.
    """
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        """
        Return a string representation of the tour object.
        """
        return self.title
    
class BandHistory(models.Model):
    """
    A class representing the band's history.

    Attributes:
        year (int): The year the event occurred.
        event (str): A description of the event.
    """
    year= models.IntegerField()
    event = models.TextField()
    
    class Meta:
        verbose_name_plural = "Band History"

    def __str__(self):
        """
        Return a string representation of the band history object.
        """
        return f"{self.year}: {self.event}"

class BandMember(models.Model):
    """
    A class representing a band member.

    Attributes:
        name (str): The name of the band member.
        instrument (str): The instrument the band member plays.
        year_joined (int): The year the band member joined (optional).
    """
    name = models.CharField(max_length=100)
    instrument = models.CharField(max_length=50)
    year_joined = models.IntegerField(null=True, blank=True)

    def __str__(self):
        """
        Return a string representation of the band member object.
        """
        return self.name

