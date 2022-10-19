from django.contrib import admin

# Register your models here.
from .models import Contact,Project

admin.site.register(Project)
admin.site.register(Contact)