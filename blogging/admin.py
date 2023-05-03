from django.contrib import admin
from .models import  *
admin.site.register(Blog)
admin.site.register(Tags)
admin.site.register(Subscribe)
admin.site.register(Comment)

