from django.contrib import admin

# Register your models here.
from .models import Contact,Project
# Register your models here.
admin.site.register(Project)
admin.site.register(Contact)