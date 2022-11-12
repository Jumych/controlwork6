from django.contrib import admin
from webapp.models import Book_Guest

# Register your models here.
class Book_GuestAdmin(admin.ModelAdmin):
    list_display = ['id,', 'name', 'email', 'description', 'deadline', 'edit_time', 'status']
    list_filter = ['status']
    search_fields = ['name']
    exclude = []

admin.site.register(Book_Guest)
