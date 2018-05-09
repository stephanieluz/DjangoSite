from django.contrib import admin
from .models import Stock
from .models import Question

admin.site.register(Question)
admin.site.register(Stock)

# Register your models here.
