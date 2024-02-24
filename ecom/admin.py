from django.contrib import admin

from .models import Product, Order

admin.site.site_header = "E-commerce Site"
admin.site.site_title = "ABC Shopping"
admin.site.index_title = "Manage ABC Shopping"

class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self, request, queryset):
        queryset.update(category="default")
    change_category_to_default.short_description = "Default category"
    actions = ('change_category_to_default',)
    
    search_fields = ('category',)
    list_display = ('title', 'price', 'discount_price', 'category', 'description', 'image',)
    fields = ('title', 'price',) # to hide other fields in detail page
    list_editable = ('price',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)