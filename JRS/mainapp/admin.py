from django.contrib import admin

# Register your models here.

from .models import jrsUser, job, companies

admin.site.register(jrsUser)
admin.site.register(job)
admin.site.register(companies)