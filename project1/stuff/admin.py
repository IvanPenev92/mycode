from django.contrib import admin

from .models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = ("page_name", "id", "title")
    list_filter = ["title"]
    search_fields = ["title"]

admin.site.register(Page, PageAdmin)