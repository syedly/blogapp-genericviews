from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(blog)
admin.site.register(comment)
admin.site.register(faq)
admin.site.register(reply)