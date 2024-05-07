from django.contrib import admin
from .models import Employee,Department,Location,JobDescription,Designation

# Register your models here.
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(JobDescription)
admin.site.register(Location)
admin.site.register(Designation)