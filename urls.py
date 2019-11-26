from django.conf.urls import url
 
from . import view
from . import loginview
# from . import jwtviews
from . import loginview

urlpatterns = [
    url('show/', view.show),
    url('images/', view.images),
    url('goodslist/', view.goodslist),
    url('categories/', view.categories),
    url('showlist/', view.showlist),
    url('login/', loginview.login),
    # url('login/', jwtviews.obtain_jwt_token),
]
