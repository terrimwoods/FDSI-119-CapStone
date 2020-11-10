
from django.db import models
from tastypie.resources import ModelResource, fields, ALL
from tastypie.authorization import Authorization
from Blog.models import Category, Article
# Create your resources here.

class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'category'
        ordering = ['id', 'name']
        filtering = {  
            'id': ALL,
            'name': ALL
        }
        allowed_methods = ['get', 'post', 'patch', 'put', 'delete', 'options']
        authorization = Authorization() # authorize all request to have write db permissions

class ArticleResource(ModelResource):
    # load the related attributes Movie => Genre
    category = fields.ToOneField(CategoryResource, 'category', full=True)
    class Meta:
        queryset = Article.objects.all()
        resource_name = 'articles'
        ordering = ['title','id','author','release_year'] 
        filtering = {
            'title': ALL,
            'author': ALL,
            'release_year': ALL,
            'article': ALL
        }
        allowed_methods = ['get', 'post', 'patch', 'put', 'delete', 'options']
        authorization = Authorization() # authorize all request to have write db permissions

"""
Run migrations everytime you modify the models

python manage.py makemigrations

python manage.py migrate
"""

"""
sample setup for my app models

from django.db import models
from tastypie.resources import ModelResource, fields, ALL
from rental.models import Movie, Genre


# Create your resources here.

class GenreResource(ModelResource):
    class Meta:
        queryset = Genre.objects.all()
        resource_name = 'genres'
        ordering = ['id', 'name']
        filtering = {  
            'id': ALL,
            'name': ALL
        }
        allowed_methods = ['get', 'post', 'patch', 'put', 'delete', 'options']
        authorization = Authorization() # authorize all request to have write db permissions


class MovieResource(ModelResource):
    # load the related attributes Movie => Genre
    genre = fields.ToOneField(GenreResource, 'genre', full=True)
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movies'
        ordering = ['title','id','price','release_year'] 
        filtering = {
            'title': ALL,
            'price': ALL,
            'release_year': ALL,
            'genre': ALL
        }
        allowed_methods = ['get', 'post', 'patch', 'put', 'delete', 'options']
        authorization = Authorization() # authorize all request to have write db permissions


Ordering:
/api/movies/?order_by=price    Asc
/api/movies/?order_by=-price   DESC



Filter:
/api/movies/?price=12  Exact eq
/api/movies/?price__lt=20  Lower than
/api/movies/?price__gt=5   greater than
/api/movies/?price__contains=forest

"""