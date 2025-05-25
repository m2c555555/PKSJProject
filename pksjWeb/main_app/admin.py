from django.contrib import admin
from .models import Paymentlist

@admin.register(Paymentlist)
class PaymentlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'transfer_date', 'status', 'slip_thumbnail')
    list_filter = ('status', 'transfer_date')
    search_fields = ('user__username', 'status')
    readonly_fields = ('slip_image_preview',)

    def slip_thumbnail(self, obj):
        if obj.slip_image:
            return f'<img src="{obj.slip_image.url}" width="80" />'
        return '-'
    slip_thumbnail.allow_tags = True
    slip_thumbnail.short_description = 'สลิป'

    def slip_image_preview(self, obj):
        if obj.slip_image:
            return f'<img src="{obj.slip_image.url}" width="300" />'
        return "No slip uploaded"
    slip_image_preview.allow_tags = True
    slip_image_preview.short_description = "ตัวอย่างสลิป"
