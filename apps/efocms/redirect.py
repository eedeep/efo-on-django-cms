import re
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth.views import auth_login
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from cms.views import details

from empcom.util.general import undecorate
from wdyt.auth.forms import WdytAuthenticationForm


# Extract the decorated details cms function for use without it's wrapper 
prepare_cms_page = undecorate(details)

def show_cms_page(request, url, additional_context):
    (template_name, context) = prepare_cms_page(request, slug=url)
    for key, val in additional_context.items():
        context[key] = val

    return render_to_response(template_name, context, context_instance=RequestContext(request))


def handle_login(request):
    context = {}
    form = WdytAuthenticationForm(request)

    if request.method == "POST":
        form = WdytAuthenticationForm(data=request.POST)
        context['next'] = request.REQUEST.get('next', '')
        if form.is_valid():
            return _login_and_redirect(request, context['next'], form)
    else:
        context['next'] = request.path_info

    context['form'] = form
    request.session.set_test_cookie()
    return show_cms_page(request, '/home/login-intervention', context)

def _login_and_redirect(request, redirect_to, login_form):
    # Light security check -- make sure redirect_to isn't garbage.
    if not redirect_to or ' ' in redirect_to:
        redirect_to = settings.LOGIN_REDIRECT_URL

    # Heavier security check -- redirects to http://example.com should
    # not be allowed, but things like /view/?param=http://example.com
    # should be allowed. This regex checks if there is a '//' *before* a
    # question mark.
    elif '//' in redirect_to and re.match(r'[^\?]*//', redirect_to):
        redirect_to = settings.LOGIN_REDIRECT_URL
    # Okay, security checks complete. Log the user in.
    auth_login(request, login_form.get_user())

    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()

    return HttpResponseRedirect(redirect_to)



