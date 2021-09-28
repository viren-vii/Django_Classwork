from django.contrib import admin
from .models import Country,City,Company, Post

# admin.site.register(City)
# admin.site.register(Country)
# admin.site.register(Subject1)


admin.site.register(Post)

class CountryAdmin(admin.ModelAdmin):


    list_display  = ['name']
    search_fields = ['name']

admin.site.register(Country,CountryAdmin)




class CityAdmin(admin.ModelAdmin):
    list_display  = ['Name', 'image_tag']

admin.site.register(City,CityAdmin)

class CompanyAdmin(admin.ModelAdmin):
	list_display = ['name']
	
admin.site.register(Company, CompanyAdmin)
