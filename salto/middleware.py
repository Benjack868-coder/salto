from django.shortcuts import redirect
from django.urls import reverse
from .settings import LOGIN_EXEMPT_URLS, SYSTEM_URLS, SYSTEM_HOME, SYSTEM_LOGIN
import re


EXEMP_URLS = []
EXEMP_URLS += [re.compile(url) for url in LOGIN_EXEMPT_URLS]


class SessionLogin:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, callback, callback_args, callback_kwargs):
        exempt_urls = []
        current_path = request.path_info.split('/')
        for url in LOGIN_EXEMPT_URLS:
            exempt_urls.append(url.strip('/'))
        if current_path[1] not in exempt_urls:
            if not request.user.is_authenticated:
                return redirect(reverse('system_login'))
            else:
                pass
        else:
            if current_path[1] in SYSTEM_URLS:
                if request.user.is_authenticated:
                    return redirect(reverse('system_index'))