from django.contrib import admin
from .models import News


# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'status')
    list_filter = ('status', 'created')
