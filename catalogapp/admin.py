from django.contrib import admin

from catalogapp.models import Product, Version


# admin.site.register(Product)

@admin.register(Product)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'is_available',)
    list_filter = ('is_available',)
    search_fields = ('name', 'description')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product_1', 'version_number', 'version_name', 'current_version',)
    list_filter = ('product_1',)
#  search_fields = ('name', 'description',)
