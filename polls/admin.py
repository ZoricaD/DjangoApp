from django.contrib import admin

from polls.models import Klient, Produkt, Prodazba, Kategorija


# Register your models here.

class ProduktInlineAdmin(admin.TabularInline):
    model = Produkt
    extra = 1


class KategorijaAdmin(admin.ModelAdmin):
    inlines = [ProduktInlineAdmin]

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    list_display = ('ime',)


class KlientAdmin(admin.ModelAdmin):
    list_display = ('ime', 'prezime',)


class ProduktAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(ProduktAdmin, self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False


admin.site.register(Klient, KlientAdmin)
admin.site.register(Produkt, ProduktAdmin)
admin.site.register(Prodazba)
admin.site.register(Kategorija, KategorijaAdmin)
