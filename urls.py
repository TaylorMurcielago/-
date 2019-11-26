from django.conf.urls import url
 
from . import view
# from . import loginview
from . import jwtviews
# from . import loginview
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView, # 生成token
#     TokenRefreshView,    # refresh tokenTestView
# )

urlpatterns = [
    url('show/', view.show),
    url('images/', view.images),
    url('goodslist/', view.goodslist),
    url('categories/', view.categories),
    url('showlist/', view.showlist),
    # url('login/', loginview.login),
    url('login/', jwtviews.obtain_jwt_token),

    # url('l1', TokenObtainPairView.as_view()),
    # url('l2', TokenRefreshView.as_view()),
    # url('l3', rest_framework_simplejwt.views.TestView.get.as_view()),
]
