from django.contrib import admin
from.models import User, Person, Students, identification_types, city, departments, countries
# Register your models here.

admin.site.register(User)
admin.site.register(Person)
admin.site.register(Students)
admin.site.register(identification_types)
admin.site.register(city)
admin.site.register(departments)
admin.site.register(countries)