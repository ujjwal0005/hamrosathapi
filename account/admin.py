from django.contrib import admin
from .models import DoctorProfile, User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

# Register your models here.
# admin.site.register(User)


class DoctorInline(admin.StackedInline):
    model = DoctorProfile
    extra=0

@admin.register(User)
class UserADmin(UserAdmin):
    # form_class = CustomUserCreationForm
    list_display=['id','email','name','number','is_active','is_doctor']
    list_display_links=['id','email',]
    ordering = ['id']
    list_filter = ['is_doctor']
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
        # elif obj and obj.is_doctor:
        #     return [DoctorInline]
        return super().get_fieldsets(request, obj)


@admin.register(DoctorProfile)
class DoctorProileAdmin(admin.ModelAdmin):
    list_display = ['user','work_experience','office_name','is_verified']
    list_filter = ['is_verified']
