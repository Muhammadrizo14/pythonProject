from django.contrib import admin

from .models import *


class RoomsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'is_published', 'teachers', 'time')
    list_display_links = ('id', 'title', 'content', 'teachers', 'time')
    search_fields = ('title', 'teachers',)
    list_filter = ('is_published', 'teachers',)
    fields = ('title', 'teachers', 'content', 'time')
    list_editable = ('is_published',)


class TeachersAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class TimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Rooms, RoomsAdmin)
admin.site.register(Teachers, TeachersAdmin)
admin.site.register(TimeGr, TimeAdmin)
