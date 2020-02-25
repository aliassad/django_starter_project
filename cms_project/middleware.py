import logging
from django.utils.deprecation import MiddlewareMixin
from constants import LOGIN_EXEMPT_URLS
from django.conf import settings
from django.shortcuts import redirect
import re
import django.conf as conf
from django.utils import timezone
import threading

# Setting logging level to Debug. By default the logging level is set to Warning.
logging.basicConfig(filename='login_middleware.log', level=logging.DEBUG)


class LoginRequiredMiddleware:
    """
    class used as middleware for whole project to allow user access for login required pages
    if only the User is logged In else redirect the user to Login page
    """
    def __init__(self, get_request):
        self.get_request = get_request

    def __call__(self, request,  *args, **kwargs):
        response = self.get_request(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        this method contains the logic where we check the User
        who is accessing the logging required page is authenticated or not also contains some code to exempt some URLs
        from login
        :param request:
        :param view_func:
        :param view_args:
        :param view_kwargs:
        :return:
        """

        path = request.path_info.lstrip('/')
        logging.debug(f'Requested path : {path}')
        url_is_exempt = path in LOGIN_EXEMPT_URLS
        if request.user.is_authenticated and url_is_exempt:
            return redirect(settings.LOGIN_REDIRECT_URL)
        elif request.user.is_authenticated or url_is_exempt:
            return None
        else:
            return redirect(settings.LOGIN_URL)


class DomainMiddleware(MiddlewareMixin):

    def process_request(self, request):
        pattern = re.compile("\\b(http://|https://|www.|.com|8000|:|//)\\W\\d+", re.I)
        words = request.get_host()
        db_name = [pattern.sub("", words)][0].split('.')[0]
        db_to_select = "cms_"+db_name
        if db_to_select != 'default':
            conf.settings.DATABASES['default']['NAME'] = db_to_select
        return None

    def process_response( self, request, response):
        return response
