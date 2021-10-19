from django.db import models

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title


class EmployeeModel(models.Model):
    fullname = models.CharField(max_length=100)
    empCode = models.CharField(max_length=5)
    mobile = models.CharField(max_length=15)
    position = models.ForeignKey(Position, on_delete=models.CASCADE,default=1)