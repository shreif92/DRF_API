from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    published_date = models.DateField()
    available = models.BooleanField(default= True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author}"



class Category(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name