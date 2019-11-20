from django.conf.urls import url
 
from . import view
from .Login import LoginView

urlpatterns = [
    url('banner/', view.hello),
    url('images/', view.images),
    url('goodslist/', view.goodslist),
    url('categories/', view.categories),
     url('showlist/', view.showlist),
     url('login/', view.login),
]
