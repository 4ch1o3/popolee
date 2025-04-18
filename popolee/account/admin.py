from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

'''# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Profile)'''


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "profile" # 복수형으로 이름 표기하지 않도록 직접 지정
    
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )

admin.site.register(User, UserAdmin) 