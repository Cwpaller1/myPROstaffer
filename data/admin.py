from django.contrib import admin
from .models import Person, Phone
from .models import Committee


# Register your models here.
admin.site.register(Person)
admin.site.register(Committee)
admin.site.register(Phone)
