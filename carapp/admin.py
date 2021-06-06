from django.contrib import admin
from .models import car
from django.utils.html import format_html
# Register your models here.
class carAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="50" style="border-radius: 10px;"/>'.format(object.photo.url))
    thumbnail.short_description ='car_image'
    list_display= ('id', 'thumbnail', 'car_title', 'model', 'price', 'fuel_type', 'is_feature')
    list_display_links =('id', 'thumbnail', 'car_title', 'model',)
    search_fields = ('car_title', 'model', 'price',)
    list_editable = ('is_feature',)
    list_filter = ('car_title','city', 'model',)
admin.site.register(car, carAdmin)