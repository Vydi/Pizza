from django.contrib import admin
from .models import Pizza


# Register your models here.


class PizzaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'description', 'price', 'image')


admin.site.register(Pizza, PizzaAdmin)
