from django.contrib import admin
from . import models


@admin.register(models.Account)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "user",
    )

@admin.register(models.Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "classification",
        "date",
        "category",
        "payment",
        "amout",
        "note",
        "status",
    )

