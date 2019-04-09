from django.contrib import admin
from .models import Person
from .models import Committee


# Register your models here.
admin.site.register(Person)
admin.site.register(Committee)