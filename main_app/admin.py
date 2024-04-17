from django.contrib import admin
# import models
from .models import Dog, Feeding, Trait
# Register your models here.
admin.site.register(Dog)
admin.site.register(Feeding)
admin.site.register(Trait)