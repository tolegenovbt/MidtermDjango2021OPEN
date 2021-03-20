from django.contrib import admin
from .models import Book, Journal
# Register your models here.

admin.site.register(Book)
admin.site.register(Journal)

# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = '__all__'
#     ordering = ['price']
#     list_editable = '__all__'
#
#
# @admin.register(Journal)
# class JournalAdmin(admin.ModelAdmin):
#     list_display = '__all__'
#     ordering = ['price']
#     list_editable = '__all__'
