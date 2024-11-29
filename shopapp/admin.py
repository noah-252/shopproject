from django.contrib import admin

from .models import Category, ShopPost,  Condition,Day,Ken

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

class ShopPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')



class ConditionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

class DayAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

class KenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

admin.site.register(Category, CategoryAdmin)
admin.site.register(ShopPost, ShopPostAdmin)
admin.site.register(Condition, ConditionAdmin)
admin.site.register(Day, DayAdmin)
admin.site.register(Ken, KenAdmin)
