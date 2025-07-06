from django.contrib import admin
from .models import Saree, SareeImage

class SareeImageInline(admin.TabularInline):
    model = SareeImage
    extra = 3  # Allows 3 image slots by default (can be more)

class SareeAdmin(admin.ModelAdmin):
    inlines = [SareeImageInline]
    list_display = ('name', 'price')

admin.site.register(Saree, SareeAdmin)

