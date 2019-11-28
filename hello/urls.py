from django.conf.urls import url
 
from . import view
from . import jwtviews
urlpatterns = [
    url('show/', view.show),
    url('images/', view.images),
    url('goodslist/', view.goodslist),
    url('categories/', view.categories),
    url('showlist/', view.showlist),
    url('login/', jwtviews.obtain_jwt_token),
]