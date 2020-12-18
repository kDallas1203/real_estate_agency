from django.contrib import admin

from .models import Flat, Claim, Owner

class OwnerInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ["owner"]

class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town']
    list_editable = ['new_building']
    list_filter = ['rooms_number', 'has_balcony', 'new_building']
    raw_id_fields = ["liked_by"]
    inlines = [OwnerInline]


class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ['flat', 'user']


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats']
    search_fields = ['full_name']


admin.site.register(Flat, FlatAdmin)
admin.site.register(Claim, ClaimAdmin)
admin.site.register(Owner, OwnerAdmin)
