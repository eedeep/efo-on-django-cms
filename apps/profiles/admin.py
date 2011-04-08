from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.db.models import get_model
from django.utils.translation import ugettext_lazy as _

# from base.admin import update_profile_meta
from profiles.utils import get_unique_username

from profiles.forms import \
    NewUserChangeForm, \
    NewUserCreationForm, \
    ProfileAdminModelForm, \
    UserAdminFormFields

class ProfileInline(admin.StackedInline):
    model = get_model('profiles', 'profile')
    can_delete = False
    max_num = 1
    form = ProfileAdminModelForm
    verbose_name = 'profile'

class UserAdmin(UserAdmin):
    
    add_form = NewUserCreationForm
    
    add_fieldsets = (
        (None, {
            'fields': (
                'first_name',
                'last_name',
                'email',
                'password1',
                'password2',
            )   
        }),
        ('Settings', {
            'fields': (
                'is_staff',
                'is_active',
                'is_superuser',
                'groups',
            )
        }),
        ('Meta', {
            'classes': ('collapse',),
            'fields': (
                'username',
                "last_login", 
                "date_joined"
            )
        }),
    )
    
    form = NewUserChangeForm
    
    inlines = [
        ProfileInline,
    ]
    
    staff_fieldsets = (
        (None, {
            'fields': (
                'first_name',
                'last_name',
                'email',
                'password',
            )   
        }),
        ('Settings', {
            'fields': (
                'is_staff',
                'is_active',
                'is_superuser',
                'groups',
            )
        }),
        ('Meta', {
            'classes': ('collapse',),
            'fields': (
                'username',
                'last_login', 
                'date_joined'
            )
        })
    )
    
    superuser_fieldsets = (
        (None, {
            'fields': (
                'first_name',
                'last_name',
                'email',
                'password',
            )   
        }),
        ('Settings', {
            'fields': (
                'is_staff',
                'is_active',
                'is_superuser',
                'groups',
            )
        }),
        ('Meta', {
            'classes': ('hide',),
            'fields': (
                'username',
                "last_login", 
                "date_joined"
            )
        }),
    )
    
    list_display = ('username', 'email', 'first_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    # prepopulated_fields = {"username": ("first_name", "last_name")}
    search_fields = ('username', 'first_name', 'email',)
    
    def change_view(self, request, *args, **kwargs):
        
        if not request.user.is_superuser:
            self.fieldsets = self.staff_fieldsets
        else:
            self.fieldsets = self.superuser_fieldsets
        
        return super(UserAdmin, self).change_view(request, *args, **kwargs)
        
    def save_formset(self, request, form, formset, change):
        """
        User admin contains a nrmal user form and an inline formset for 
        profiles with a single inline. When a user instance is created 
        its related profile is automatically created also, and when the 
        profile inline is saved here, the profile instance already exists 
        and therefore causes an integrity error in the DB. So when we are 
        adding a new user below, only save the user form itself - don't 
        save the formset and then update the profile object that was 
        automatically created with the values extract directly from 
        request.POST, ignoring the formset entirely.
        """
        
        # When updating an change_form_templateexisting user, behave as normal.
        if change:
            return super(UserAdmin, self).save_formset(request, form, 
                                                       formset, change)
        # Save the user
        user = form.save()
        user.save()
        profile = user.get_profile()
        prefix = "profile_set-0-"
        
        # Go through each field in request.POST - if it has a value and 
        # is prefixed with the profile inline prefix and is not a field 
        # on the profile that already has a value (such as the user itself) 
        # then assign it to the profile object.
        for k, v in request.POST.items():
            if v and k.startswith(prefix):
                k = k.replace(prefix, "")
                if hasattr(profile, k) and not getattr(profile, k):
                    setattr(profile, k, v)
        profile.save()
        
    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.username = get_unique_username(obj.first_name, obj.last_name)
        return super(UserAdmin, self).save_model(request, obj, form, change)
        
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
