from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

# Register your models here.
# admin.site.register(User)


@admin.register(User)
class UserADmin(UserAdmin):
    # form_class = CustomUserCreationForm
    list_display=['id','email','name','number','is_staff','is_active','is_doctor']
    list_display_links=['id','email',]
    ordering = ['id']
    # readonly_fields = ('date_joined','last_login')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('name','number')}),
        (_('Permissions'), {
            'fields': ('is_doctor','is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login',)}),
    )

    customer_fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('name','number')}),
        (_('Permissions'), {
            'fields': ('is_active',),
        }),
        (_('Important dates'), {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','name','number', 'password1', 'password2','is_staff','is_doctor'),
        }),
    )


    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)

