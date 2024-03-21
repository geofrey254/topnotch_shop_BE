import sys
from django.db import models

# CATEGORY MODEL


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "categories"

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name


class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.CharField(max_length=400)
    price = models.IntegerField(null=True)
    front_thumbnail = models.FileField(upload_to='images/', null=True)
    back_thumbnail = models.FileField(upload_to='images/', null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    published = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-published']
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title
