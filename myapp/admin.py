from django.contrib import admin
from myapp.models import auther,books,auther1
# Register your models here.

@admin.register(auther)
class autheradmin(admin.ModelAdmin):
    list_display = ['aname','age']

@admin.register(books)
class booksadmin(admin.ModelAdmin):
    list_display = ['bname']

@admin.register(auther1)
class auther1admin(admin.ModelAdmin):
    list_display = ['aname','age','written']