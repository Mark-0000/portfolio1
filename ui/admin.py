from django.contrib import admin

from .models import Project, Message

# Register your models here.
admin.site.register(Project)
admin.site.register(Message)
admin.site.site_header = 'N I N E'
admin.site.site_title = 'N I N E'
# admin.site.index_title = 'N I N E'

