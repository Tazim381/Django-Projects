from django.db import models

# Create your models here.

class Book(models.Model):
    title =models.CharField(db_column='title',max_length=1000,blank=False) #title,description,author,year are coloms in database
    description =models.CharField(db_column='description',max_length=1000,blank=False)
    author =models.CharField(db_column='author',max_length=1000,blank=False)
    year=models.IntegerField(db_column='year',max_length=1000,blank=False)

