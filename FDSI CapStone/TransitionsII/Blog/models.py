from django.db import models
from django.utils import timezone


# Run migrations everytime you modify the models
# python manage.py makemigrations
# python manage.py migrate

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    image_url = models.TextField()
    blog_entry = models.TextField()
    date_created = models.DateTimeField(default = timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
        
    def __str__(self):
        return self.title + "|"+ str(self.author) + "|" + str(self.blog_entry)