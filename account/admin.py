from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import Account


class AccountAdmin(UserAdmin):
    # list_display = ('email', 'username', 'cnic', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    list_display = ('email', 'CNIC', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    # search_fields = ('email', 'username', 'cnic')
    search_fields = ('email', 'CNIC')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'CNIC', 'password1', 'password2'),
        }),
    )

    ordering = ('-date_joined',)


admin.site.register(Account, AccountAdmin)
