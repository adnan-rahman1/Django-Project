from django.contrib import admin
# Register your models here.

from .models import Todos

admin.site.register(Todos)

