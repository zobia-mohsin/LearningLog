from django.contrib import admin

# Register your models here.
from .models import Topic, Entry
#from .models import Entry
admin.site.register(Topic)
admin.site.register(Entry)