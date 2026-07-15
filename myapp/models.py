from django.db import models

# Create your models here.

class Type(models.Model):
    nomi = models.CharField(max_length=30)
    def __str__(self):
        return self.nomi

class Portfolio(models.Model):
    nomi = models.CharField(max_length=30)
    company_name = models.CharField(max_length=50)
    date = models.DateField()
    url = models.URLField()
    malumot = models.TextField()
    tur = models.ForeignKey(Type, on_delete=models.CASCADE)
    rasm1 = models.ImageField(upload_to='media')
    rasm2 = models.ImageField(upload_to='media', null=True, blank=True)
    rasm3 = models.ImageField(upload_to='media', null=True, blank=True)
