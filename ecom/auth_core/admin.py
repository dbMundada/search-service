from django.contrib.auth.models import Group as DjangoGroup
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from my_admin.admin import admin_site
from auth_core.models import User

class UserAdmin(DjangoUserAdmin):
    
    def __init__(self, salary):
        self.salary = salary;
        
    def getSalary(cls):
        return cls.salary

admin_site.register(User, UserAdmin)
