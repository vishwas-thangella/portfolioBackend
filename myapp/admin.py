from django.contrib import admin
from myapp import models

# Register your models here.

admin.site.register(models.HomeData)
admin.site.register(models.Skills)
admin.site.register(models.Projects)
admin.site.register(models.Education)
admin.site.register(models.Experience)
admin.site.register(models.Contact)