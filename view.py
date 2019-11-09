from django.http import HttpResponse

import json
from django.http.response import JsonResponse

def hello(request):
   data = {
        "dataList": [
                         {
                            "name": "布尔信息林州上线了！", "id": 0, "businessId": 0, "picUrl": "https://www.lcpww.cn/images/1.jpg"
                             },
                             {
                            "name": "布尔信息林州欢迎您！！", "id": 1, "businessId": 1, "picUrl": "https://www.lcpww.cn/images/2.jpg"
                             }
                ],
        "code": 0
        }

   return JsonResponse(data)


def images(request):
    data = {
        "images": [
                         {
                            "id": 0, "businessId": 0, "picUrl": "https://www.lcpww.cn/images/1.jpg"
                             },
                             {
                            "id": 1, "businessId": 1, "picUrl": "https://www.lcpww.cn/images/2.jpg"
                             },
                              {
                            "id": 2, "businessId": 1, "picUrl": "https://www.lcpww.cn/images/3.jpg"
                             },
                              {
                            "id": 3, "businessId": 1, "picUrl": "https://www.lcpww.cn/images/1.jpg"
                             }
                ],
        "code": 0
        }

    return JsonResponse(data)


def goodslist(request):
    data = {
        "data": [
                        {
                            "id": 0, "businessId": 0, "pic": "https://www.lcpww.cn/images/1.jpg", "name": "lisan11", "jobtype": "会计", "height": "165", "education": "本科",
                            "characteristic": "a11", "minPrice": 50, "originalPrice": 20, "numberOrders": 3, "starscore": 20, "recommendStatus": "true",
                            "xuanxiang": ["26岁", "166cm", "会计", "林州", "擦李"],
                            "renzheng":["真人认证", "学历认证", "家长认证"]
                             },
                             {
                            "id": 1, "businessId": 1, "pic": "https://www.lcpww.cn/images/2.jpg", "name": "zhangsi22", "jobtype": "公务员", "height": "163", "education": "专科",
                            "characteristic": "b22", "minPrice": 60, "originalPrice": 14, "numberOrders": 90, "starscore": 20, "recommendStatus": "false",
                            "xuanxiang": ["22岁", "161cm", "老师", "林州"],
                            "renzheng":["真人认证", "学历认证"]
                             },
                             {
                            "id": 2, "businessId": 0, "pic": "https://www.lcpww.cn/images/1.jpg", "name": "lisan33", "jobtype": "老师", "height": "166", "education": "硕士",
                            "characteristic": "a33", "minPrice": 30, "originalPrice": 20, "numberOrders": 3, "starscore": 20, "recommendStatus": "true",
                            "xuanxiang": ["26岁", "166cm", "会计", "林州", "擦李"],
                            "renzheng":["真人认证", "学历认证", "家长认证"]
                             },
                             {
                            "id": 3, "businessId": 1, "pic": "https://www.lcpww.cn/images/2.jpg", "name": "zhangsi44", "jobtype": "快递员", "height": "160", "education": "高中",
                            "characteristic": "b44", "minPrice": 200, "originalPrice": 14, "numberOrders": 90, "starscore": 20, "recommendStatus": "false",
                            "xuanxiang": ["29岁", "166cm", "会计", "林州"],
                            "renzheng":["真人认证", "学历认证"]
                             },
                             {
                            "id": 4, "businessId": 0, "pic": "https://www.lcpww.cn/images/1.jpg", "name": "lisan55", "jobtype": "无业", "height": "162", "education": "初中",
                            "characteristic": "a55", "minPrice": 100, "originalPrice": 20, "numberOrders": 3, "starscore": 20, "recommendStatus": "true",
                            "xuanxiang": ["23岁", "166cm", "会计", "林州", "擦李"],
                            "renzheng":["真人认证", "学历认证", "家长认证"]
                             },
                             {
                            "id": 5, "businessId": 1, "pic": "https://www.lcpww.cn/images/2.jpg", "name": "zhangsi66", "jobtype": "会计", "height": "165", "education": "本科",
                            "characteristic": "b66", "minPrice": 80, "originalPrice": 14, "numberOrders": 90, "starscore": 20, "recommendStatus": "false",
                            "xuanxiang": ["22岁", "166cm", "会计", "林州"],
                            "renzheng":["真人认证", "学历认证"]
                             },
                             {
                            "id": 6, "businessId": 0, "pic": "https://www.lcpww.cn/images/1.jpg", "name": "lisan77", "characteristic": "a88", "jobtype": "会计", "height": "165", "education": "本科",
                            "minPrice": 10, "originalPrice": 50, "numberOrders": 3, "starscore": 20, "recommendStatus": "true",
                            "xuanxiang": ["24岁", "166cm", "会计", "林州"],
                            "renzheng":["真人认证", "学历认证", "家长认证"]
                             },
                             {
                            "id": 7, "businessId": 1, "pic": "https://www.lcpww.cn/images/2.jpg", "name": "zhangsi88", "characteristic": "b99", "jobtype": "会计", "height": "165", "education": "本科",
                            "minPrice": 12.1, "originalPrice": 50, "numberOrders": 90, "starscore": 20, "recommendStatus": "false",
                            "xuanxiang": ["21岁", "166cm", "会计", "林州"],
                            "renzheng":["真人认证", "学历认证"]
                             }

                ],
        "code": 0
        }

    return JsonResponse(data)


def categories(request):
    data = {
        "data": [
                         {
                            "id": 0, "key": 'key1', "type": "jiaju2", "name": "lisan2", "characteristic": "a2", "minPrice": 10,
                            "originalPrice": 20, "numberOrders": 3, "starscore": 20, "recommendStatus": "true"
                             },
                             {
                            "id": 1, "key": "key2", "type": "shenghuo2", "name": "zhangsi2", "characteristic": "b2", "minPrice": 12.1,
                            "originalPrice": 14, "numberOrders": 90, "starscore": 20, "recommendStatus": "true"
                             }
                ],
        "code": 0
        }

    return JsonResponse(data)


def showlist(request):
    data = {
        "pics": [
                         {
                            "id": 0, "businessId": 0, "pic": "https://www.lcpww.cn/images/4.jpg", "name": "lisan11", "jobtype": "会计", "height": "165", "education": "本科",
                            "characteristic": "a11", "minPrice": 10, "originalPrice": 20, "numberOrders": 3, "starscore": 20, "recommendStatus": "true",
                            "xuanxiang": ["26岁", "166cm", "会计", "林州", "擦李"],
                            "renzheng":["真人认证", "学历认证", "家长认证"]
                             },
                             {
                            "id": 1, "businessId": 1, "pic": "https://www.lcpww.cn/images/5.jpg", "name": "zhangsi22", "jobtype": "公务员", "height": "163", "education": "专科",
                            "characteristic": "b22", "minPrice": 12.1, "originalPrice": 14, "numberOrders": 90, "starscore": 20, "recommendStatus": "false",
                            "xuanxiang": ["22岁", "161cm", "老师", "林州"],
                            "renzheng":["真人认证", "学历认证"]
                             },
                             {
                            "id": 1, "businessId": 1, "pic": "https://www.lcpww.cn/images/6.jpg", "name": "zhangsi22", "jobtype": "公务员", "height": "163", "education": "专科",
                            "characteristic": "b22", "minPrice": 12.1, "originalPrice": 14, "numberOrders": 90, "starscore": 20, "recommendStatus": "false",
                            "xuanxiang": ["22岁", "161cm", "老师", "林州"],
                            "renzheng":["真人认证", "学历认证"]
                             },
                             {
                            "id": 1, "businessId": 1, "pic": "https://www.lcpww.cn/images/7.jpg", "name": "zhangsi22", "jobtype": "公务员", "height": "163", "education": "专科",
                            "characteristic": "b22", "minPrice": 12.1, "originalPrice": 14, "numberOrders": 90, "starscore": 20, "recommendStatus": "false",
                            "xuanxiang": ["22岁", "161cm", "老师", "林州"],
                            "renzheng":["真人认证", "学历认证"]
                             }
                ],
        "basicInfo": [
                         {
                            "id": 0, "businessId": 0, "pic": "https://www.lcpww.cn/images/4.jpg", "name": "绝色猫咪", "jobtype": "会计", "height": "165", "education": "本科",
                            "commissionType": 1, "commission": 100, "selectSizePrice": "1111", "numberOrders": 23, "numberGoodReputation": 46, "minPrice": 10, "originalPrice": 20, "numberOrders": 3, "starscore": 20, "recommendStatus": "true",
                            "xuanxiang": ["26岁", "166cm", "会计", "林州", "擦李"],
                            "renzheng":["真人认证", "学历认证", "家长认证"]
                             }
                ],
        "singlecharacter": [
                            {
                            "id": 0, "businessId": 0, "pic": "https://www.lcpww.cn/images/1.jpg", "name": "lisan11", "jobtype": "会计", "height": "165", "education": "本科",
                            "characteristic": "a11", "minPrice": 50, "originalPrice": 20, "numberOrders": 3, "starscore": 20, "recommendStatus": "true",
                            "xuanxiang": ["26岁", "166cm", "会计", "林州", "擦李"],
                            "renzheng":["真人认证", "学历认证", "家长认证"]
                             },
                             {
                            "id": 1, "businessId": 1, "pic": "https://www.lcpww.cn/images/2.jpg", "name": "zhangsi22", "jobtype": "公务员", "height": "163", "education": "专科",
                            "characteristic": "b22", "minPrice": 60, "originalPrice": 14, "numberOrders": 90, "starscore": 20, "recommendStatus": "false",
                            "xuanxiang": ["22岁", "161cm", "老师", "林州"],
                            "renzheng":["真人认证", "学历认证"]
                             },
                             {
                            "id": 2, "businessId": 0, "pic": "https://www.lcpww.cn/images/1.jpg", "name": "lisan33", "jobtype": "老师", "height": "166", "education": "硕士",
                            "characteristic": "a33", "minPrice": 30, "originalPrice": 20, "numberOrders": 3, "starscore": 20, "recommendStatus": "true",
                            "xuanxiang": ["26岁", "166cm", "会计", "林州", "擦李"],
                            "renzheng":["真人认证", "学历认证", "家长认证"]
                             },
                             {
                            "id": 3, "businessId": 1, "pic": "https://www.lcpww.cn/images/2.jpg", "name": "zhangsi44", "jobtype": "快递员", "height": "160", "education": "高中",
                            "characteristic": "b44", "minPrice": 200, "originalPrice": 14, "numberOrders": 90, "starscore": 20, "recommendStatus": "false",
                            "xuanxiang": ["29岁", "166cm", "会计", "林州"],
                            "renzheng":["真人认证", "学历认证"]
                             },
                             {
                            "id": 4, "businessId": 1, "pic": "https://www.lcpww.cn/images/2.jpg", "name": "zhangsi22", "jobtype": "公务员", "height": "163", "education": "专科",
                            "characteristic": "b22", "minPrice": 60, "originalPrice": 14, "numberOrders": 90, "starscore": 20, "recommendStatus": "false",
                            "xuanxiang": ["22岁", "161cm", "老师", "林州"],
                            "renzheng":["真人认证", "学历认证"]
                             },
                             {
                            "id": 5, "businessId": 0, "pic": "https://www.lcpww.cn/images/1.jpg", "name": "lisan33", "jobtype": "老师", "height": "166", "education": "硕士",
                            "characteristic": "a33", "minPrice": 30, "originalPrice": 20, "numberOrders": 3, "starscore": 20, "recommendStatus": "true",
                            "xuanxiang": ["26岁", "166cm", "会计", "林州", "擦李"],
                            "renzheng":["真人认证", "学历认证", "家长认证"]
                             },
                             {
                            "id": 6, "businessId": 1, "pic": "https://www.lcpww.cn/images/2.jpg", "name": "zhangsi44", "jobtype": "快递员", "height": "160", "education": "高中",
                            "characteristic": "b44", "minPrice": 200, "originalPrice": 14, "numberOrders": 90, "starscore": 20, "recommendStatus": "false",
                            "xuanxiang": ["29岁", "166cm", "会计", "林州"],
                            "renzheng":["真人认证", "学历认证"]
                             }  
                ]
        }

    return JsonResponse(data)
