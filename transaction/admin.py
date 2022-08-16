from django.contrib import admin
from .models import Transaction


#@admin.register(Account)
#class AccountAdmin(admin.ModelAdmin):
#    list_display = ("Name",)
#    search_fields = ("Name",)


@admin.register(Transaction)
class AccountTransaction(admin.ModelAdmin):
    list_display = ("Amount", "Type", "Category", "Date", "Client")
    search_fields = ("Category",)
