from django.db import models

class Cinema(models.Model):
    name=models.CharField(max_length=20)
    year=models.IntegerField()
    rating=models.DecimalField(max_digits=10,decimal_places=1)
    genre=models.TextField()
    image=models.ImageField(upload_to='movies',null=True,blank=True)
    def __str__(self):
        return self.name
