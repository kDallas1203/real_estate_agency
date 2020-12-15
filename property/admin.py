from django.contrib import admin

from .models import Flat, Claim


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town']
    list_editable = ['new_building']
    list_filter = ['rooms_number', 'has_balcony', 'new_building']


class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ['flat', 'user']


admin.site.register(Flat, FlatAdmin)
admin.site.register(Claim, ClaimAdmin)
