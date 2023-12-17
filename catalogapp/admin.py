from django.contrib import admin

from catalogapp.models import Product


# admin.site.register(Product)

@admin.register(Product)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'is_available',)
    list_filter = ('is_available',)
    search_fields = ('name', 'description')


#@admin.register(Category)
#class CategoryAdmin(admin.ModelAdmin):
 #   list_display = ('id', 'name', 'description',)
  #  search_fields = ('name', 'description',)
