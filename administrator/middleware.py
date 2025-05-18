# administrator/middleware.py
from django.http import HttpResponseForbidden
from django.conf import settings

class AdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path.startswith('adminpage'):
            if not request.user.is_authenticated or not request.user.is_staff:
                from django.contrib.auth.views import redirect_to_login
                return redirect_to_login(request.path)
        return None
