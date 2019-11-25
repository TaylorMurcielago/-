from django.conf.urls import url
 
from . import view
# from .Login import LoginView

urlpatterns = [
    # url('banner/', view.banner),
    url('show/', view.show),
    url('images/', view.images),
    url('goodslist/', view.goodslist),
    url('categories/', view.categories),
     url('showlist/', view.showlist),
    #  url('login/', view.login),
]
