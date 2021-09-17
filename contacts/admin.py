from contacts.models import Contacts
from django.contrib import admin


class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'phone_number', 'created_date')


admin.site.register(Contacts, ContactAdmin)
