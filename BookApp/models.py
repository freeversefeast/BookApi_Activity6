from django.db import models

# Create your models here.
class Books(models.Model):
    BookId = models.AutoField(primary_key=True)
    BookName = models.CharField(max_length=500)
    BookQuantity = models.IntegerField()
    BookGenre = models.CharField(max_length=500)
    BookBestSeller = models.CharField(max_length=500)