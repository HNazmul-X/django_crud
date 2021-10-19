from django.contrib import admin

from employe.models import EmployeeModel, Position

# Register your models here.
admin.site.register(EmployeeModel)
admin.site.register(Position)