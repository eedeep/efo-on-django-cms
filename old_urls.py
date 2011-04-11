from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import databrowse
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

from pinax.apps.account.openid_consumer import PinaxConsumer
from pinax.apps.account.urls import signup_view
from profiles.forms import LoginForm, SignupForm


handler500 = "pinax.views.server_error"

urlpatterns = patterns("",
    # url(r"^$", direct_to_template, {
    #         "template": "homepage.html",
    #     }, name="home"),
    
    url(r"^account/signup/$", signup_view, {"form_class": SignupForm},
        name="acct_signup"),
        
    url(r'^account/login/validate/$', 
        'ajax_validation.views.validate', 
        {'form_class': LoginForm}, 
        'acct_login_validate'),
        
    url(r"^account/login/$", 
        "pinax.apps.account.views.login", 
        {"form_class": LoginForm},
        name="acct_login"),

    url(r"^$", "landings.views.home", name="home"),
    url(r"^tags/", include("tags.urls")),
    url(r"^projects/", include("projects.urls")),
    url(r"^programmes/", include("programmes.urls")),
    url(r"^profiles/", include("profiles.urls")),
    url(r"^search/", include("search.urls")),
    url(r"^inbox/", include("inbox.urls")),
    
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^db/(.*)', databrowse.site.root),
    
    url(r"^admin/invite_user/$", "pinax.apps.signup_codes.views.admin_invite_user", name="admin_invite_user"),
    url(r"^admin/", include(admin.site.urls), name="admin"),
    url(r"^about/", include("about.urls")),
    
    url(r"^account/admin/login/$", 
        "pinax.apps.account.views.login", 
        kwargs={ 
            'success_url': '/admin',
            'redirect_field_name': 'admin_redirect',
            'redirect_field_value': '/admin',
            'template_name': 'admin/login.html', },
        name="admin_login"),
        
    url(r"^account/logout/$", 
        "base.views.logout",
        {
            "template_name": "account/logout.html",
            "next_page": "/"
        }, name="logout"),
        
    url(r"^account/", include("pinax.apps.account.urls")),
    url(r"^openid/(.*)", PinaxConsumer()),
    
    url(r"^notices/", include("notification.urls")),
    url(r"^announcements/", include("announcements.urls")),
    
    (r'^grappelli/', include('grappelli.urls')),
    (r'^admin/filebrowser/', include('filebrowser.urls')),
    url(r'^admin_tools/', include('admin_tools.urls')),
    
)


if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        url(r"", include("staticfiles.urls")),
    )
