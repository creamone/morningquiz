#user/models.py
from django.db import models


# Create your models here.
class Article(models.Model):
    class Meta:
        db_table = "article"

    title = models.CharField(max_length=20, null=False)
    category = models.CharField(max_length=256, null=False)
    content = models.CharField(max_length=256, default='')


class Category(models.Model):
    class Meta:
        db_table = "category"
    category_name = models.CharField(max_length=256)
    category_content = models.CharField(max_length=256)
