from django.contrib import admin

# Register your models here.
from django.contrib import admin
from boards.models import Board

admin.site.register(Board)