from django.contrib import admin

# Register your models here.
from .models import Blog
class blogAdmin(admin.ModelAdmin):
    list_display = ('id','blog_tittle','author_name',"blog_date")
    search_fields = ('id','blog_tittle','author_name')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Blog,blogAdmin)
admin.site.site_header ="Sinbad Admin"




