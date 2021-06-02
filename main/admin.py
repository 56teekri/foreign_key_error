from django.contrib import admin
from .models import Book, Author, Publications, Teacher, Student

# Register your models here.
admin.site.register([Book, Author, Publications, Teacher, Student])
