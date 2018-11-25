from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(post)
admin.site.register(contact)
admin.site.register(User)
admin.site.register(banned)
admin.site.register(notifications)