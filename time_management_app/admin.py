from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'task_name', 'category', 'priority', 'status', 'starting_date', 'ending_date')
    list_filter = ('user', 'category', 'priority', 'status', 'starting_date', 'ending_date')
    search_fields = ('task_name', 'category', 'priority', 'status', 'starting_date', 'ending_date')

    fieldsets = (
        ('General Information', {
            'fields': ('user', 'task_name', 'description', 'notes')
        }),
        ('Time Information', {
            'fields': ('starting_time', 'ending_time', 'starting_date', 'ending_date', 'days_of_week')
        }),
        ('Task Properties', {
            'fields': ('category', 'priority', 'status')
        }),
    )

    readonly_fields = ('user',)

    def save_model(self, request, obj, form, change):
        if not change:
            # Set the user field only on the first save (creation)
            obj.user = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Task, TaskAdmin)
