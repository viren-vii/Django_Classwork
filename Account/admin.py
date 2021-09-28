from django.contrib import admin
from .models import Acc_information


class Acc_information_Admin(admin.ModelAdmin):


    list_per_page = 2

    list_display  = ['name','subject']
    search_fields = ['name']


admin.site.register(Acc_information, Acc_information_Admin)


# Register your models here.
