from django.contrib import admin
from .models import Thread, Subforo, Post

# Register your models here.
admin.site.register(Thread)
admin.site.register(Subforo)
admin.site.register(Post)
