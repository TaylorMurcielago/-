from django.views.generic.base import View
from django.http import HttpResponse

class LoginView(View):
    def get(self, request):
        info = request.META.get('HTTP_USER_AGENT', 'unknown')
        return HttpResponse("Your browser is %s" % info)

    def post(self, request):
         return '321321'    # get请求所执行的函数