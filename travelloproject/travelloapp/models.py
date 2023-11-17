from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Destiny(models.Model):
    img=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=200)
    desc=models.TextField()

    def __str__(self):
        return self.name
class People(models.Model):
    photo=models.ImageField(upload_to='pic')
    person=models.CharField(max_length=200)
    design=models.TextField()

    def __str__(self):
        return self.person