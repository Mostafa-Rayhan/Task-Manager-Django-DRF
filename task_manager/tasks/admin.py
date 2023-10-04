from django.contrib import admin
from .models import Task, Photo

class PhotoInline(admin.TabularInline):
    model = Photo

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'priority', 'completion_status', 'user')
    list_filter = ('priority', 'completion_status')
    search_fields = ('title',)
    inlines = [PhotoInline]
    ordering = ('-priority',)

admin.site.register(Task, TaskAdmin)
admin.site.register(Photo)
