from django.contrib import admin
from .models import Books, Category

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ("name",)
    search_fields = ['name']


admin.site.register(Category, CategoryAdmin)


class BooksAdmin(admin.ModelAdmin):
    list_display = ["title", "author"]
    list_filter = ("title", "price",)
    search_fields = ['title']


admin.site.register(Books, BooksAdmin)
