from django.db import models
from django.contrib import admin
class footballplayer (models.Model):
    numofmatch=models.IntegerField()
    name=models.CharField(max_length=100)
    salary=models.IntegerField()
    age=models.IntegerField()
    height=models.IntegerField()

class footballplayerAdmin(admin.ModelAdmin):
    list_display=('numofmatch','name','salary','age','height')