from django.contrib import admin
from .models import Article, Categorie, MessageContact, Service
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'auteur', 'date_pub')
    list_filter = ('categorie', 'date_pub')
    search_fields = ('titre', 'contenu')
    prepopulated_fields = {'slug': ('titre',)}
class CategorieAdmin(admin.ModelAdmin):
    search_fields = ('nom',)
@admin.register(MessageContact)
class MessageContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'sujet', 'date_envoye')
    search_fields = ('nom', 'email', 'sujet', 'message')
    list_filter = ('date_envoye',)
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('titre', 'created')
    search_fields = ('titre', 'description')
    list_filter = ('created',)
    prepopulated_fields = {'slug': ('titre',)}
admin.site.register(Article, ArticleAdmin)
admin.site.register(Categorie, CategorieAdmin)


from django.contrib import admin
from .models import FAQ
class FAQInline(admin.TabularInline):  # Ou admin.StackedInline pour un affichage différent
    model = FAQ
    extra = 1
    fields = ('question', 'reponse', 'ordre')
    ordering = ('ordre',)
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'service', 'ordre')
    list_filter = ('service',)
    search_fields = ('question', 'reponse')
    ordering = ('service', 'ordre')

    from .models import Service
class ServiceAdmin(admin.ModelAdmin):
    inlines = [FAQInline]
    # ... gardez vos autres configurations existantes
# Si Service est déjà enregistré, il faut d'abord le désenregistrer
admin.site.unregister(Service)
admin.site.register(Service, ServiceAdmin)