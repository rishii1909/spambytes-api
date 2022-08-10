from django.contrib import admin

from apps.user.models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = (
        "uuid", "email_address"
    )
    search_fields = ["uuid", "email_address"]


admin.site.register(User)
