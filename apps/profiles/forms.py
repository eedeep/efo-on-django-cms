from django import forms
from django.contrib import admin
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User, Group
from django.contrib.sites.models import Site
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import get_model
from django.forms.widgets import FileInput, Textarea, HiddenInput, TextInput
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from pinax.apps.account.forms import SignupForm as PinaxSignupForm
from pinax.apps.account.forms import LoginForm as PinaxLoginForm
from emailconfirmation.models import EmailAddress

from profiles.utils import get_unique_username
from profiles.models import Profile

import settings

REQUIRED_EMAIL = getattr(settings, "ACCOUNT_REQUIRED_EMAIL", False)
EMAIL_VERIFICATION = getattr(settings, "ACCOUNT_EMAIL_VERIFICATION", False)
EMAIL_AUTHENTICATION = getattr(settings, "ACCOUNT_EMAIL_AUTHENTICATION", False)
UNIQUE_EMAIL = getattr(settings, "ACCOUNT_UNIQUE_EMAIL", False)

class FieldOrderingMixin(object):
    """
    Mixin form forms that will force the field order defined by the 
    attribute ``field_order``.
    """
    def __init__(self, *args, **kwargs):
        """
        Apply custom sorting to the form fields.
        """
        super(FieldOrderingMixin, self).__init__(*args, **kwargs)
        sort_func = lambda x: (self.field_order + self.fields.keyOrder).index(x)
        self.fields.keyOrder = sorted(self.fields.keyOrder, key=sort_func)

class LoginForm(PinaxLoginForm):
    """
    Subclass Pinax's Login form to change a few things.
    """
    
    def clean(self):
        if self._errors:
            return
        user = authenticate(**self.user_credentials())
        if user:
            if user.is_active:
                self.user = user
            else:
                if EMAIL_AUTHENTICATION:
                    try:
                        emailaddress = EmailAddress.objects.get(email=user.email)
                    except ObjectDoesNotExist:
                        """
                        Email address does not exist? The emailaddress may have
                        been removed, or this user created via admin, in this case
                        we'll just show the account inactive msg.
                        """
                        raise forms.ValidationError(_("This account is currently inactive."))
                    else:
                        if not emailaddress.verified:
                            raise forms.ValidationError(
                                _("This account is currently inactive due to an unverified email address.  Check your email for a verification message from noreply@architecturenow.com."))
                else:
                    raise forms.ValidationError(_("This account is currently inactive."))
        else:
            if EMAIL_AUTHENTICATION:
                error = _("The e-mail address and/or password you specified are not correct.")
            else:
                error = _("The username and/or password you specified are not correct.")
            raise forms.ValidationError(error)
        return self.cleaned_data

class SignupForm(FieldOrderingMixin, PinaxSignupForm):
    """
    Subclass Pinax's SignupForm so that we can customize the fields. This 
    form class is then brought into the root url conf and used as a keyword
    arg to the overridding signup urlpattern.
    """

    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    subscribe = forms.BooleanField(label="", required=False, initial=True, 
                    help_text="Sign me up for the ANow newsletter - the latest projects, opinions, news and events")
    # Hide ``PinaxSignupForm.username``.
    username = forms.CharField(required=False, widget=forms.HiddenInput())
        
    field_order = ["first_name", "last_name", "email"]

    def clean_username(self):
        """
        This field is hidden and unused so it should always validate.
        """
        return True

    def create_user(self, username=None, commit=True):
        """
        Create a username based on first and last names, then create the user.
        """
        first_name = self.cleaned_data["first_name"]
        last_name = self.cleaned_data["last_name"]
        username = get_unique_username(first_name, last_name) 
        user = super(SignupForm, self).create_user(username, False)
        user.first_name = first_name
        user.last_name = last_name
        if commit:
            user.save()
        return user

class ProfileAccountForm(FieldOrderingMixin, forms.ModelForm):
    
    first_name = forms.CharField(
        max_length=30,
        required=True,)
    last_name = forms.CharField(
        max_length=30,
        required=True,)
    email = forms.EmailField(
        max_length=30,
        required=True,)
    password1 = forms.CharField(
        label="Password (if changing)", 
        required=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'off'}, render_value=False))
    password2 = forms.CharField(
        label="Password (again)", 
        required=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'off'}, render_value=False))
    subscribe = forms.BooleanField(
        help_text="Sign me up for the ANow newsletter - the latest projects, opinions, news and events",
        initial=True, 
        label="", 
        required=False)
    location = forms.CharField(
        label="Location", 
        required=False)
        
    profession = forms.CharField(
        label="Occupation", 
        required=False)
        
    biography = forms.CharField(
        label="Bio",
        required=False,
        widget=Textarea)

    field_order = [
        "first_name", 
        "last_name", 
        "email", 
        "password1", 
        "password2",
        "avatar",
        "profession",
        "location",
        "biography",]

    class Meta:
        model = Profile
        fields = (
            "avatar",
            "location",
            "profession", 
            "biography",)
        exclude = ("is_contributor",)
        widgets = {
            'avatar': FileInput,
            'biography': Textarea,
            'is_contributor': HiddenInput,
        }
    
    def __init__(self, *args, **kwargs):
        initial = kwargs.pop("initial", {})
        profile = kwargs["instance"]
        user = profile.user
        initial["first_name"] = user.first_name
        initial["last_name"] = user.last_name
        initial["email"] = user.email
        initial["location"] = profile.location
        kwargs["initial"] = initial
        super(ProfileAccountForm, self).__init__(*args, **kwargs)
    
    def clean(self):
        """
        Ensure password fields match if either are entered.
        """
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data.get("password2", "")
        if (password1 or password2) and password1 != password2:
            raise forms.ValidationError(_("You must type the same password each time."))
        return self.cleaned_data

    def save(self, *args, **kwargs):
        """
        Update any non-profile fields such as those on the user object.
        """
        profile = super(ProfileAccountForm, self).save(*args, **kwargs)
        user = profile.user
        first_name = self.cleaned_data["first_name"]
        last_name = self.cleaned_data["last_name"]
        if user.first_name != first_name or user.last_name != last_name:
            # Create a new unique username if the profile changes
            # their firstname or lastname.
            user.username = get_unique_username(first_name, last_name)
        password = self.cleaned_data.get("password1", "")
        if password:
            user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.email = self.cleaned_data["email"]
        user.save()
        return profile
        
class ContributorAccountForm(ProfileAccountForm):
    
    class Meta:
        model = Profile
        widgets = {
            'avatar': HiddenInput,
        }
        exclude = [
            "user",
            "first_name",
            "last_name",
            "occupation",
            "street",
            "suburb",
            "city",
            "state",
            "country",
            "post_code",
            "biography",
            "website",
            "site",
        ]
        

# Hack
class ContributorAccountForm(FieldOrderingMixin, forms.ModelForm):
    
    first_name = forms.CharField(
        max_length=30,
        required=True,)
    last_name = forms.CharField(
        max_length=30,
        required=True,)
    email = forms.EmailField(
        max_length=30,
        required=True,)
    password1 = forms.CharField(
        label="Password (if changing)", 
        required=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'off'}, render_value=False))
    password2 = forms.CharField(
        label="Password (again)", 
        required=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'off'}, render_value=False))
    subscribe = forms.BooleanField(
        help_text="Sign me up for the ANow newsletter - the latest projects, opinions, news and events",
        initial=True, 
        label="", 
        required=False)
    location = forms.CharField(
        label="Location", 
        required=False,
        widget=TextInput(attrs={'disabled': 'disabled'},))
        
    profession = forms.CharField(
        label="Occupation", 
        required=False,
        widget=TextInput(attrs={'disabled': 'disabled'},))
        
    biography = forms.CharField(
        label="Bio",
        required=False,
        widget=Textarea(attrs={'disabled': 'disabled'},))

    field_order = [
        "first_name", 
        "last_name", 
        "email", 
        "password1", 
        "password2",
        "avatar",
        "profession",
        "location",
        "biography",]

    class Meta:
        model = Profile
        fields = (
            "avatar",
            "location",
            "profession", 
            "biography",)
        exclude = ("is_contributor",)
        widgets = {
            'avatar': HiddenInput,
            'biography': Textarea,
            'is_contributor': HiddenInput,
        }
    
    def __init__(self, *args, **kwargs):
        initial = kwargs.pop("initial", {})
        profile = kwargs["instance"]
        user = profile.user
        initial["first_name"] = user.first_name
        initial["last_name"] = user.last_name
        initial["email"] = user.email
        initial["location"] = profile.location
        kwargs["initial"] = initial
        super(ContributorAccountForm, self).__init__(*args, **kwargs)
    
    def clean(self):
        """
        Ensure password fields match if either are entered.
        """
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data.get("password2", "")
        if (password1 or password2) and password1 != password2:
            raise forms.ValidationError(_("You must type the same password each time."))
        return self.cleaned_data

    def save(self, *args, **kwargs):
        """
        Update any non-profile fields such as those on the user object.
        """
        profile = super(ContributorAccountForm, self).save(*args, **kwargs)
        user = profile.user
        first_name = self.cleaned_data["first_name"]
        last_name = self.cleaned_data["last_name"]
        if user.first_name != first_name or user.last_name != last_name:
            # Create a new unique username if the profile changes
            # their firstname or lastname.
            user.username = get_unique_username(first_name, last_name)
        password = self.cleaned_data.get("password1", "")
        if password:
            user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.email = self.cleaned_data["email"]
        user.save()
        return profile        
        
"""
Admin forms
"""

class HorizRadioRenderer(forms.RadioSelect.renderer):
    """ this overrides widget method to put radio buttons horizontally
        instead of vertically.
    """
    def render(self):
        """Outputs radios"""
        return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

YesNoRadio = forms.RadioSelect(
    choices=(
        (True, 'Yes'),
        (False, 'No')
    ),
    renderer=HorizRadioRenderer)
    
class ProfileAdminModelForm(forms.ModelForm):
    
    
    
    class Meta:
        model = get_model('profiles', 'profile')        
        widgets = {
            'is_contributor': YesNoRadio,
        }
    class Media:
        css = {
            'all': (
                '/site_media/static/admin/css/grappelli-skin-basic.css',
                '/site_media/static/admin/css/grappelli-skin-defaults.css',
                '/site_media/static/admin/css/buttons.css',
                '/site_media/static/filebrowser/css/filebrowser.css',)
        }

class UserAdminFormFields(forms.ModelForm):
    
    first_name = forms.CharField(
        max_length=255,
        required=True)
    last_name = forms.CharField(
        max_length=255,
        required=True)
    email = forms.EmailField(
        label=_("E-mail"), 
        max_length=75,
        required=True)
    username = forms.RegexField(label=_("Username"), max_length=30, regex=r'^[\w.@+-]+$',
        help_text = _("Auto-generated. 30 characters or fewer. Letters, digits and @/./+/-/_ only."),
        error_messages = {'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters.")},
        required=False,
        widget=HiddenInput())
        
    is_staff = forms.BooleanField(
        help_text="Designates whether the user can log into this admin site.",
        initial=False,
        label=_("Is staff"),
        required=False,
        widget=YesNoRadio)
        
    is_active = forms.BooleanField(
        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.", 
        initial=True,
        label=_("Active"),
        required=False,
        widget=YesNoRadio)
        
    is_superuser = forms.BooleanField(
        help_text="Designates that this user has all permissions without explicitly assigning them.",
        initial=False,
        label=_("Administrator"),
        required=False,
        widget=YesNoRadio)
        
    """
    Currently, use of class Meta: with widgets
    seems to throw an unrelated error in the UserChangeForm
    missing 'password' field.
    
    For now, is_staff, is_active & is_superuser need to be
    specified explicity, as above.
    """    
        
    # class Meta:
    #     widgets = {
    #         'is_staff': YesNoRadio,
    #         'is_active': YesNoRadio,
    #         'is_superuser': YesNoRadio,
    #     }
    
class NewUserCreationForm(UserCreationForm, UserAdminFormFields):
    pass
    # class Meta:
    #     widgets = {
    #         'is_staff': YesNoRadio,
    #         'is_active': YesNoRadio,
    #         'is_superuser': YesNoRadio,
    #     }

class NewUserChangeForm(UserChangeForm, UserAdminFormFields):
    pass
    # class Meta:
    #     widgets = {
    #         'is_staff': YesNoRadio,
    #         'is_active': YesNoRadio,
    #         'is_superuser': YesNoRadio,
    #     }
        
# ======= deprecate below?
        
# class ProfileAccountForm(forms.ModelForm):
#     
#     password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
#     password2 = forms.CharField(label=_("Confirm password"), widget=forms.PasswordInput,
#         help_text = _("Enter the same password as above, for verification."))
#     
#     class Meta:
#         model = Profile
#         widgets = {
#             'avatar': FileInput,
#         }    