from django.contrib import admin

# Register your models here.
from .models import LearnPlace, Certification


admin.site.register(LearnPlace)
admin.site.register(Certification)
