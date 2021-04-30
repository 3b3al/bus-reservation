from django.contrib import admin
from .models import Bus, User, Book



admin.site.site_header = "booking admin"
admin.site.site_title = "booking Admin Area"
admin.site.index_title = "welcome to the booking admin area"
# Register your models here.

admin.site.register(Bus)
admin.site.register(User)
admin.site.register(Book)


