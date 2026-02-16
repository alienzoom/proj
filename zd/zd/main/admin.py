from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from .models import CustomUser
from .models_application import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'organization_name', 'solution_name', 'created_at', 'status']
    list_filter = ['status', 'created_at']
    search_fields = ['organization_name', 'contact_email']
    
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser

class CustomUserCreationFormAdmin(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name')

class CustomUserAdmin(UserAdmin):
   
    list_display = ('email', 'username', 'first_name', 'last_name', 'phone_number', 'is_staff', 'is_active', 'is_superuser')
    
    search_fields = ('email', 'username', 'first_name', 'last_name', 'phone_number')
    
    list_filter = ('is_staff', 'is_active', 'is_superuser', 'date_joined')
   
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'middle_name', 'email', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
  
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'phone_number'),
        }),
    )
  
    form = CustomUserChangeForm
    add_form = CustomUserCreationFormAdmin
    
    ordering = ('-date_joined',)  
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        
        return qs


admin.site.register(CustomUser, CustomUserAdmin)