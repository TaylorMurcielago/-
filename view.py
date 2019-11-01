from django.http import HttpResponse
 
import json
from django.http.response import JsonResponse

def hello(request):
   data = {
        "dataList": [
                         {
                            "name":"布尔信息林州上线了！" , "id":0,"businessId":0,"picUrl":"https://www.lcpww.cn/images/1.jpg"
                             },
                             {
                            "name":"布尔信息林州欢迎您！！" , "id":1,"businessId":1,"picUrl":"https://www.lcpww.cn/images/2.jpg"
                             }
                ],
        "code":0
        }
   
   return JsonResponse(data)
def images(request):
    data = {
        "images": [
                         {
                            "id":0,"businessId":0,"picUrl":"https://www.lcpww.cn/images/1.jpg"
                             },
                             {
                            "id":1,"businessId":1,"picUrl":"https://www.lcpww.cn/images/2.jpg"
                             },
                              {
                            "id":2,"businessId":1,"picUrl":"https://www.lcpww.cn/images/3.jpg"
                             },
                              {
                            "id":3,"businessId":1,"picUrl":"https://www.lcpww.cn/images/1.jpg"
                             }
                ],
        "code":0
        }
   
    return JsonResponse(data)
def goodslist(request):
    data = {
        "data": [
                         {
                            "id":0,"businessId":0,"pic":"https://www.lcpww.cn/images/1.jpg","name":"lisan1","characteristic":"a1",
                            "minPrice":10,"originalPrice":20,"numberOrders":3,"starscore":20,"recommendStatus":"true"
                             },
                             {
                            "id":1,"businessId":1,"pic":"https://www.lcpww.cn/images/2.jpg","name":"zhangsi1","characteristic":"b1",
                            "minPrice":12.1,"originalPrice":14,"numberOrders":90,"starscore":20,"recommendStatus":"false"
                             }
                ],
        "code":0
        }
   
    return JsonResponse(data)
def categories(request):
    data = {
        "data": [
                         {
                            "id":0,"key":'key1',"type":"jiaju2","name":"lisan2","characteristic":"a2","minPrice":10,
                            "originalPrice":20,"numberOrders":3,"starscore":20,"recommendStatus":"true"
                             },
                             {
                            "id":1,"key":"key2","type":"shenghuo2","name":"zhangsi2","characteristic":"b2","minPrice":12.1,
                            "originalPrice":14,"numberOrders":90,"starscore":20,"recommendStatus":"true"
                             }
                ],
        "code":0
        }
   
    return JsonResponse(data)
def showlist(request):
    data = {
        "data": [
                         {
                            "id":0,"businessId":0,"pic":"https://www.lcpww.cn/images/1.jpg","name":"lisan11","jobtype":"会计","height":"165","education":"本科",
                            "characteristic":"a11","minPrice":10,"originalPrice":20,"numberOrders":3,"starscore":20,"recommendStatus":"true"
                             },
                             {
                            "id":1,"businessId":1,"pic":"https://www.lcpww.cn/images/2.jpg","name":"zhangsi22","jobtype":"公务员","height":"163","education":"专科",
                            "characteristic":"b22","minPrice":12.1,"originalPrice":14,"numberOrders":90,"starscore":20,"recommendStatus":"false"
                             },
                             {
                            "id":2,"businessId":0,"pic":"https://www.lcpww.cn/images/1.jpg","name":"lisan33","jobtype":"老师","height":"166","education":"硕士",
                            "characteristic":"a33","minPrice":10,"originalPrice":20,"numberOrders":3,"starscore":20,"recommendStatus":"true"
                             },
                             {
                            "id":3,"businessId":1,"pic":"https://www.lcpww.cn/images/2.jpg","name":"zhangsi44","jobtype":"快递员","height":"160","education":"高中",
                            "characteristic":"b44","minPrice":12.1,"originalPrice":14,"numberOrders":90,"starscore":20,"recommendStatus":"false"
                             },
                             {
                            "id":4,"businessId":0,"pic":"https://www.lcpww.cn/images/1.jpg","name":"lisan55","jobtype":"无业","height":"162","education":"初中",
                            "characteristic":"a55","minPrice":10,"originalPrice":20,"numberOrders":3,"starscore":20,"recommendStatus":"true"
                             },
                             {
                            "id":5,"businessId":1,"pic":"https://www.lcpww.cn/images/2.jpg","name":"zhangsi66","jobtype":"会计","height":"165","education":"本科",
                            "characteristic":"b66","minPrice":12.1,"originalPrice":14,"numberOrders":90,"starscore":20,"recommendStatus":"false"
                             },
                             {
                            "id":6,"businessId":0,"pic":"https://www.lcpww.cn/images/1.jpg","name":"lisan77","characteristic":"a88","jobtype":"会计","height":"165","education":"本科",
                            "minPrice":10,"originalPrice":20,"numberOrders":3,"starscore":20,"recommendStatus":"true"
                             },
                             {
                            "id":7,"businessId":1,"pic":"https://www.lcpww.cn/images/2.jpg","name":"zhangsi88","characteristic":"b99","jobtype":"会计","height":"165","education":"本科",
                            "minPrice":12.1,"originalPrice":14,"numberOrders":90,"starscore":20,"recommendStatus":"false"
                             }
                ],
        "code":0
        }
   
    return JsonResponse(data)
