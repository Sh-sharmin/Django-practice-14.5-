from django.db import models
import datetime
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField(default='..@gmail.com')
    Article_no= models.BigIntegerField(default=0)
    publish = models.BooleanField(default=False)
    date = models.DateField(default=datetime.date.today)
    date_time = models.DateTimeField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    file = models.FileField(upload_to='uploads/', null=True, blank=True) 
    def __str__(self):
        return self.name