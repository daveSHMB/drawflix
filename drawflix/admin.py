from django.contrib import admin
from drawflix.models import Drawing

# list display attributes of a drawing in the admin panel
class DrawingAdmin(admin.ModelAdmin):

    list_display = ('film', 'user', 'likes', 'date')

admin.site.register(Drawing, DrawingAdmin)
