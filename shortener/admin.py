from django.contrib import admin

from .models import ShortenedLink

class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'link', 'shortened_link', 'creation_date', 'user_ip', 'user_agent')
    list_filter = ('creation_date',)


admin.site.register(ShortenedLink, LinkAdmin)
