from django.contrib import admin
from .models import Board


# Register your models here.
# 在这里，我们可以添加用户和组来管理权限

admin.site.register(Board)