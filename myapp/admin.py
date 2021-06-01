from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="30" style="border-radius: 40px;"/>'.format(object.photo.url))
    thumbnail.short_description ='image'
    list_display= ('id','thumbnail','first_name','last_name','desination','created_date')
    list_display_links =('id','thumbnail','first_name',)
    search_fields = ('first_name','last_name','desination',)
    list_filter = ('desination',)
admin.site.register(Team, TeamAdmin)