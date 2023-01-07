from django.contrib import admin
from .models import Project
 
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'img_preview')
    readonly_fields = ('img_preview',)

    def img_preview(self, obj):
        return obj.img_preview

    img_preview.short_description = 'Preview'
    img_preview.allow_tags = True

admin.site.register(Project, ProjectAdmin)