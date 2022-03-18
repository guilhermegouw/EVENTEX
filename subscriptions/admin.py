from django.contrib import admin
from django.utils.timezone import now

from subscriptions.models import Subscription


class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "cpf", "created_at", "subscriped_today")
    date_hierarchy = "created_at"
    search_fields = ("name", "email", "phone", "created_at")
    list_filter = ("created_at",)

    def subscriped_today(self, obj):
        return obj.created_at == now().date()

    subscriped_today.short_description = "inscrito hoje?"
    subscriped_today.boolean = True


admin.site.register(Subscription, SubscriptionModelAdmin)
