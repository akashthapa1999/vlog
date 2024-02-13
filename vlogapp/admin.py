from django.contrib import admin
from vlogapp.models import vlogDetails

# Register your models here.

class vlogpage(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "Date", "img", 'email', 'thought')

admin.site.register(vlogDetails, vlogpage)