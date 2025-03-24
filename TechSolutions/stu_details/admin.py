from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register([Gender,students,billing,courses,Duration,Batch,expences,accounts])
