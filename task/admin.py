from django.contrib import admin

from task.models import Profileimg, Tasklist

# Register your models here.
admin.site.register(Tasklist)
admin.site.register(Profileimg)