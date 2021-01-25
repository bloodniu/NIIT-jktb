# -*- coding:UTF-8 -*-
# Copyright (c) 2020 tx All rights reserved.
#   XXX

import requests
import json
import time
import datetime
import logging
import ast
import yaml
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header

logging.getLogger().setLevel(logging.INFO)

with open('config.yaml', 'r',encoding='utf-8') as config:
    information = yaml.load(config.read(), Loader=yaml.FullLoader)
    number = information['number']
    Name = information['Name']
    amap_key = information['amap_key']
    Cookie = information['Cookie']
    X_CSRF_Token = information['X_CSRF_Token']
    Province_GPS = information['Province_GPS']
    City_GPS = information['City_GPS']
    District_GPS = information['District_GPS']
    Detail_GPS = information['Detail_GPS']

time_ = int(str(int(time.time())).ljust(13,'0'))
create_time = datetime.datetime.utcnow()
format_date = time.strftime( "%Y-%m-%d", time.localtime())
ts = time.strptime(format_date, "%Y-%m-%d")
date_ = int(str(int(time.mktime(ts))).ljust(13, '0'))
format_date_1 = time.strftime( "%Y%m%d", time.localtime())
format_date_2 = time.strftime( "%Y%m%d-", time.localtime())
value = number
xxx = str(hex(0x5e528599eeb8c80000000000 ))[2:]                      #个人身份编码
yyy = str(hex(0x5e5285946dd054f090000000 ))[2:]                      #班级身份编码
zzz = str(hex(0x5e5285946dd054f090000000 ))[2:]                      #学院身份编码
Class = ''
Name = Name
name = ''
telephone = ''
null = ''
t = round(time.time() * 1000)

def location_get_itude(Province_GPS, City_GPS, District_GPS, Detail_GPS, amap_key):
    logging.info("\033[1;32m ** jktb开始 ** \033[0m")
    amap_API_url_get_L = 'https://restapi.amap.com/v3/geocode/geo?address={}&key={}'.format(Province_GPS + City_GPS + District_GPS + Detail_GPS, amap_key)
    GPS = requests.get(amap_API_url_get_L)
    GPS = str(ast.literal_eval(GPS.text)['geocodes'])[1:-1]
    GPS = ast.literal_eval(GPS)['location'].split(",")
    Longitude = GPS[0].ljust(7, '0')
    print(" 当前经度：" + Longitude)
    Latitude = GPS[1].ljust(7, '0')
    print(" 当前纬度：" + Latitude)
    location_get_itude = []
    location_get_itude.append(Longitude)
    location_get_itude.append(Latitude)
    return location_get_itude

push_data = time.strftime(number + "%Y%m%d", time.localtime())
logging.info("\033[1;32m ** Get ready ** \033[0m")

session = requests.Session()

url_start_ready_1 = 'https://wxwork.jiandaoyun.com/wxwork/wx7fbebe04b23f59a4/dashboard'
header_start_ready_1 = {
    'host': 'wxwork.jiandaoyun.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-Encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'if-none-match': 'W/"a38-eV/rktb3RMEAhLb9lg80BMCQURE"',
    'referer': 'https://wxwork.jiandaoyun.com/wxwork/wx7fbebe04b23f59a4/dashboard',
    'user-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 wxwork/3.0.25 MicroMessenger/7.0.1 Language/zh',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'cookie': Cookie
}

url_start_ready_2 = 'https://wxwork.jiandaoyun.com/dashboard/apps'
header_start_ready_2 = {
    'host':'wxwork.jiandaoyun.com',
    'accept':'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    "content-length":'2',
    'content-type': 'application/json;charset=UTF-8',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    'origin':'https://wxwork.jiandaoyun.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer':'https://wxwork.jiandaoyun.com/wxwork/wx7fbebe04b23f59a4/dashboard',
    'x-jdy-ver': '2.43.2',
    'x-csrf-token': X_CSRF_Token,
    'Cookie': Cookie
}
data_start_ready_2 = {
    'corpId': 'wx7fbebe04b23f59a4'
}

url ='wxwork.jiandaoyun.com/corp/login_user_info'
header000={
    'host': 'wxwork.jiandaoyun.com',
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    "content-length": '2',
    'content-type': 'application/json;charset=UTF-8',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    'origin': 'https://wxwork.jiandaoyun.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://wxwork.jiandaoyun.com/wxwork/wx7fbebe04b23f59a4/dashboard',
    'x-jdy-ver': '2.43.2',
    'x-csrf-token': X_CSRF_Token,
    'Cookie': Cookie

}

url_start_ready_3 = 'https://wxwork.jiandaoyun.com/dashboard/workflow/todo_count'
header_start_ready_3 = header_start_ready_2
data_start_ready_3 = data_start_ready_2

url_start_ready_4 = 'https://track.jiandaoyun.com/log?u=wx7fbebe04b23f59a4-{}&c=wx7fbebe04b23f59a4&t={}&e=custom_app_post_m'.format(t, number)
header_start_ready_4 = {
    'Host': 'track.jiandaoyun.com',
    "content-length": '0',
    'user-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 wxwork/3.0.25 MicroMessenger/7.0.1 Language/zh',
    'content-type': 'application/json;charset=UTF-8',
    'accept': '*/*',
    'origin': 'https://wxwork.jiandaoyun.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-dest': 'empty',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Referer': 'https://wxwork.jiandaoyun.com',
    "cookie":Cookie
}

url_ready_1 = "https://track.jiandaoyun.com/log?u=wx7fbebe04b23f59a4-{}&c=wx7fbebe04b23f59a4&t={}&e=app_visit_from_mobile".format(t, number)
header_ready_1 = header_start_ready_4

url_ready_2 = 'https://wxwork.jiandaoyun.com/_/app/5e3b8676c3668d000638849a'
header_ready_2 = {
    'Host': 'wxwork.jiandaoyun.com',
    'content-length':'2',
    'Accept': 'application/json, text/plain, */*',
    'X-JDY-Ver': '2.43.2',
    'X-CSRF-Token': X_CSRF_Token,
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://wxwork.jiandaoyun.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'Referer': 'https://wxwork.jiandaoyun.com/wxwork/ww0f8c29c5c7b53b53/dashboard',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cookie': Cookie
}
data_ready_2 = {
    'appId': '5e3b8676c3668d000638849a'
}

url_ready_3 = 'https://wxwork.jiandaoyun.com/_/app/5e3b8676c3668d000638849a/workflow/query_data_count'
header_ready_3 = header_ready_2
data_ready_3 = {
    'type': 'todo'
}

url_1 = 'https://wxwork.jiandaoyun.com/_/app/5e3b8676c3668d000638849a/form/5e523eefb635060006aab416'
header = {
    'host': 'wxwork.jiandaoyun.com',
    'accept': 'application/json, text/plain, */*',
    'X-JDY-Ver': '2.43.2',
    'X-CSRF-Token': X_CSRF_Token,
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://wxwork.jiandaoyun.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'Referer': 'https://wxwork.jiandaoyun.com/wxwork/wx7fbebe04b23f59a4/dashboard',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cookie': Cookie

}
data_1 = {
    "appId": "5e3b8676c3668d000638849a",
    "entryId": "5e523eefb635060006aab416"
}

url_middle = 'https://wxwork.jiandaoyun.com/_/app/5e3b8676c3668d000638849a/get_vip_pack'
header_middle = header_ready_2
data_middle = data_1

url_all = 'https://wxwork.jiandaoyun.com/_/data/link'
data_2_1 ={
        "formId": "5e528e0c9a3a2700064bbe0d",
        "appId": "5e3b8676c3668d000638849a",
        "entryId": "5e523eefb635060006aab416",
        "filter": {
            "rel": "and",
            "cond": [
                {
                    "entryId": "5e528e0c9a3a2700064bbe0d",
                    "value": [yyy],
                    "method": "eq",
                    "type": "dept",
                    "field": "_widget_1582468620961"
                }
            ]
        },
        "field": "_widget_1582468620958",
        "refAppId": "5da7c38a0e29bb0006ef96fd"
}
# get data 1
data_2_2 = {
        "formId": "5e54021ddba2a900067e3e52",
        "appId": "5e3b8676c3668d000638849a",
        "entryId": "5e523eefb635060006aab416",
        "filter": {
            "rel": "and",
            "cond": [
                {
                    "entryId": "5e54021ddba2a900067e3e52",
                    "value": [value],
                    "method": "eq",
                    "type": "text",
                    "field": "_widget_1582563869969"
                }
            ]
        },
        "field": "_widget_1582563869968",
        "refAppId": "5da7c38a0e29bb0006ef96fd"

}
# get data 2
data_2_3 = {
        "formId": "5e54021ddba2a900067e3e52",
        "appId": "5e3b8676c3668d000638849a",
        "entryId": "5e523eefb635060006aab416",
        "filter": {
            "rel": "and",
            "cond": [
                {
                    "entryId": "5e54021ddba2a900067e3e52",
                    "value": [value],
                    "method": "eq",
                    "type": "text",
                    "field": "_widget_1582563869969"
                }
            ]
        },
        "field": "_widget_1582596235172",
        "refAppId": "5da7c38a0e29bb0006ef96fd"
}
# get data 3
data_2_4 = {
        "formId": "5e54021ddba2a900067e3e52",
        "appId": "5e3b8676c3668d000638849a",
        "entryId": "5e523eefb635060006aab416",
        "filter": {
            "rel": "and",
            "cond": [
                {
                    "entryId": "5e54021ddba2a900067e3e52",
                    "value": [value],
                    "method": "eq",
                    "type": "text",
                    "field": "_widget_1582563869969"
                }
            ]
        },
        "field": "_widget_1582563869971",
        "refAppId": "5da7c38a0e29bb0006ef96fd"
}
# get data 4
data_2_5 = {
        "formId": "5e54021ddba2a900067e3e52",
        "appId": "5e3b8676c3668d000638849a",
        "entryId": "5e523eefb635060006aab416",
        "filter": {
            "rel": "and",
            "cond": [
                {
                    "entryId": "5e54021ddba2a900067e3e52",
                    "value": [value],
                    "method": "eq",
                    "type": "text",
                    "field": "_widget_1582563869969"
                }
            ]
        },
        "field": "_widget_1582563869972",
        "refAppId": "5da7c38a0e29bb0006ef96fd"

}
# get data 5
data_2_6 = {
        "formId": "5e54021ddba2a900067e3e52",
        "appId": "5e3b8676c3668d000638849a",
        "entryId": "5e523eefb635060006aab416",
        "filter": {
            "rel": "and",
            "cond": [
                {
                    "entryId": "5e54021ddba2a900067e3e52",
                    "value": [value],
                    "method": "eq",
                    "type": "text",
                    "field": "_widget_1582563869969"
                }
            ]
        },
        "field": "_widget_1582563869973",
        "refAppId": "5da7c38a0e29bb0006ef96fd"
}
# get data 6
data_2_7 = {
    "formId": "5e54021ddba2a900067e3e52",
    "appId": "5e3b8676c3668d000638849a",
    "entryId": "5e523eefb635060006aab416",
    "filter": {
        "rel": "and",
        "cond": [
            {
                "entryId": "5e54021ddba2a900067e3e52",
                "value": [value],
                "method": "eq",
                "type": "text",
                "field": "_widget_1582563869969"
            }
        ]
    },
    "field": "_widget_1582563869976",
    "refAppId": "5da7c38a0e29bb0006ef96fd"
}
# get data 7
data_2_8 = {
        "formId": "5e54021ddba2a900067e3e52",
        "appId": "5e3b8676c3668d000638849a",
        "entryId": "5e523eefb635060006aab416",
        "filter": {
            "rel": "and",
            "cond": [
                {
                    "entryId": "5e54021ddba2a900067e3e52",
                    "value": [value],
                    "method": "eq",
                    "type": "text",
                    "field": "_widget_1582563869969"
                }
            ]
        },
        "field": "_widget_1582604297261",
        "refAppId": "5da7c38a0e29bb0006ef96fd"
}
# get data 8
data_2_9 = {
        "formId": "5e54021ddba2a900067e3e52",
        "appId": "5e3b8676c3668d000638849a",
        "entryId": "5e523eefb635060006aab416",
        "filter": {
            "rel": "and",
            "cond": [
                {
                    "entryId": "5e54021ddba2a900067e3e52",
                    "value": [value],
                    "method": "eq",
                    "type": "text",
                    "field": "_widget_1582563869969"
                }
            ]
        },
        "field": "_widget_1583760540221",
        "refAppId": "5da7c38a0e29bb0006ef96fd"

}
# get data 9
data_2_10 = {
        "formId": "5e528e0c9a3a2700064bbe0d",
        "appId": "5e3b8676c3668d000638849a",
        "entryId": "5e523eefb635060006aab416",
        "filter": {
            "rel": "and",
            "cond": [
                {
                    "entryId": "5e528e0c9a3a2700064bbe0d",
                    "value": [Class],
                    "method": "eq",
                    "type": "text",
                    "field": "_widget_1582801445210"
                }
            ]
        },
        "field": "_widget_1582801445696",
        "refAppId": "5da7c38a0e29bb0006ef96fd"
}
# get data 10

url_push = 'https://wxwork.jiandaoyun.com/_/data/create'

if __name__ == '__main__':
    Detail_GPS_push = Detail_GPS
    District_GPS_push = District_GPS
    Province_GPS_push = Province_GPS
    City_GPS_push = City_GPS
    list_itude = location_get_itude(Province_GPS, City_GPS, District_GPS, Detail_GPS, amap_key)
    Longitude_push = list_itude[0]
    Latitude_push = list_itude[1]


    time.sleep(1)
    re = session.get(url_start_ready_1, headers = header_start_ready_1, timeout = 20)
    print(re.status_code)
    re = session.post(url_start_ready_2, headers = header_start_ready_2, data = json.dumps(data_start_ready_2), timeout = 20)
    print(re.status_code)
    re = session.post(url_start_ready_3, headers = header_start_ready_3, data = json.dumps(data_start_ready_3), timeout = 20)
    print(re.status_code)
    re = session.get(url_start_ready_4, headers = header_start_ready_4, timeout = 20)
    print(re.status_code)
    re = session.get(url_ready_1, headers = header_ready_1, timeout = 20)
    print(re.status_code)
    re = session.post(url_ready_2, headers = header_ready_2, data = json.dumps(data_ready_2), timeout = 20)
    print(re.status_code)
    re = session.post(url_ready_3, headers = header_ready_3, data = json.dumps(data_ready_2), timeout = 20)
    print(re.status_code)
    re = session.post(url_1, headers = header, data = json.dumps(data_1), timeout = 20)
    print(' get if seccess ' + str(re.status_code))
    re = session.post(url_middle, headers = header_middle, data = json.dumps(data_middle), timeout = 20)
    print(str(re.status_code))
    logging.info("\033[1;32m all ready to start ! \033[0m")
    re = session.post(url_all, headers = header, data = json.dumps(data_2_1), timeout = 20)
    _id = ast.literal_eval(re.text)['value']['_id']
    name = ast.literal_eval(re.text)['value']['name']
    username = ast.literal_eval(re.text)['value']['username']
    print(' get id ' + _id + name + username)
    re = session.post(url_all, headers = header, data = json.dumps(data_2_2), timeout = 20)
    Class = ast.literal_eval(re.text)['value']
    print(' get Class ' + Class)
    re = session.post(url_all, headers = header, data = json.dumps(data_2_3), timeout = 20)
    email = ast.literal_eval(re.text)['value']
    print(' get email ' + email)
    re = session.post(url_all, headers = header, data = json.dumps(data_2_4), timeout = 20)
    sex = ast.literal_eval(re.text)['value']
    print(' get sex ' + sex)
    re = session.post(url_all, headers=header, data=json.dumps(data_2_5), timeout=20)
    telephone = ast.literal_eval(re.text)['value']
    print(' get telephone ' + telephone)
    re = session.post(url_all, headers=header, data=json.dumps(data_2_6), timeout=20)
    grade = ast.literal_eval(re.text)['value']
    print(' get grade ' + grade)
    re = session.post(url_all, headers=header, data=json.dumps(data_2_7), timeout=20)
    sdept = ast.literal_eval(re.text)['value']
    print(' get sdept ' + sdept)
    re = session.post(url_all, headers=header, data=json.dumps(data_2_10), timeout=20)
    b = re.status_code
    re = session.post(url_all, headers=header, data=json.dumps(data_2_9), timeout=20)
    Province = ast.literal_eval(re.text)['value']['province']
    City = ast.literal_eval(re.text)['value']['city']
    District = ast.literal_eval(re.text)['value']['district']
    Detail = ast.literal_eval(re.text)['value']['detail']
    print(' get address ' + Province + City + District + Detail)
    re = session.post(url_all, headers=header, data=json.dumps(data_2_8), timeout=20)
    a = re.status_code

    if a == 200 and b == 200:
        logging.info("\033[1;31m 信息全部获取完毕 \033[0m")

    logging.info("\033[1;31m ** Wait two seconds ** \033[0m")
    time.sleep(2)

    data_push ={
        "values": {
            "_widget_1582451693412": {
                "data": time_,
                "visible": 'true'
            },
            "_widget_1582448368018": {
                "data": yyy,
                "visible": 'true'
            },
            "_widget_1582448367786": {
                "data": xxx,
                "visible": 'true'
            },
            "_widget_1582448367861": {
                "data": number,
                "visible": 'true'
            },
            "_widget_1582733225657": {
                "data": Name,
                "visible": 'false'
            },
            "_widget_1582714895053": {
                 "data": Class,
                "visible": 'false'
            },
            "_widget_1583053730857": {
                "data": email,
                "visible": 'false'
            },
            "_widget_1582644793959": {
                "data": sex,
                "visible": 'false'
            },
            "_widget_1582451694455": {
                "data": telephone,
                "visible": 'false'
            },
            "_widget_1582448367945": {
                "data": sdept,
                "visible": 'false'
            },
            "_widget_1582699228446": {
                "data": zzz,
                "visible": 'false'
            },
            "_widget_1582448368277": {
                "data": grade,
                "visible": 'false'
            },
            "_widget_1582448368427": {
                "data": "正常",
                "visible": 'true'
            },
            "_widget_1582448368936": {
                "data": {"province":Province,
                         "city": City,
                         "district": District},
                "visible": 'true'
            },
            "_widget_1583388441010": {
                "data": {"province": Province,
                         "city": City,
                         "district": District,
                         "detail": Detail},
                "visible": 'true'
            },
            "_widget_1582448368502": {
                "data": {"province": Province_GPS_push,
                         "city": City_GPS_push,
                         "district": District_GPS_push,
                         "detail": Detail_GPS_push,
                     "lnglatXY": [Longitude_push, Latitude_push]},
                "visible": 'true'
            },
            "_widget_1582448368629": {
                "visible": 'false'
            },
            "_widget_1582451690218": {
                "data": "无",
                "visible": 'true'
            },
            "_widget_1582451690319": {
                "visible": 'false'
            },
            "_widget_1582451690487": {
                "data": "否",
                "visible": 'true'
            },
            "_widget_1582451690399": {
                "data": "否",
                "visible": 'true'
            },
            "_widget_1598314516966": {
                "data": "否",
                "visible": 'true'
            },
            "_widget_1582451690673": {
                "data": "无",
            "visible": 'true'
            },
            "_widget_1582451691487": {
                "visible": 'false'
            },
            "_widget_1582451690718": {
                "visible": 'false'
            },
            "_widget_1582451690816": {
                "visible": 'false'
            },
            "_widget_1582451690851": {
                "visible": 'false'
            },
            "_widget_1602519244699": {
                "data": "否",
                "visible": 'true'
            },
            "_widget_1582451690888": {
                "data": "否，未途经",
                "visible": 'true'
            },
            "_widget_1598314517267": {
                "data": "否，未停留",
                "visible": 'true'
            },
            "_widget_1582632750681": {
                "visible": 'false'
            },
            "_widget_1582451692104": {
                "data": "否，无接触史",
                "visible": 'true'
            },
            "_widget_1582632750765": {
                "visible": 'false'
            },
            "_widget_1585658093803": {
                "data": "无",
                "visible": 'true'
            },
            "_widget_1585658093820": {
                "visible": 'false'
            },
            "_widget_1585658093866": {
                "data": "否，无接触",
                "visible": 'true'
            },
            "_widget_1585658093916": {
                "visible": 'false'
            },
            "_widget_1585658093928": {
                "visible": 'false'
            },
            "_widget_1585658094079": {
                "visible": 'false'
            },
            "_widget_1585658094125": {
                "data": "否，无接触",
                "visible": 'true'
            },
            "_widget_1585658094147": {
                "visible": 'false'
            },
            "_widget_1582451692339": {
                "visible": 'false'
            },
            "_widget_1582451692681": {
                "data": "是，已联系告知",
                "visible": 'true'
            },
            "_widget_1582451692740": {
                "data": "是",
                "visible": 'false'
            },
            "_widget_1582451692841": {
                "data": "是",
                "visible": 'true'
            },
            "_widget_1582451692971": {
                "data": "",
                "visible": 'true'
            },
            "_widget_1582644794365": {
                "data": _id,
                "visible": 'false'
            },
            "_widget_1583544091720": {
                "data": username,
                "visible": 'false'
            },
            "_widget_1583566000982": {
                "data": name,
                "visible": 'false'
            },
            "_widget_1582451693522": {
                "data": format_date_1,
                "visible": 'false'
            },
            "_widget_1582964633122": {
                "data": "正常",
                "visible": 'true'
            },
            "_widget_1582451693649": {
                "data": format_date_2+number,
                "visible": 'false'
            },
            "_widget_1582729327347": {
                "data": 1,
                "visible": 'false'
            }
        },
        "appId": "5e3b8676c3668d000638849a",
        "entryId": "5e523eefb635060006aab416",
        "formId": "5e523eefb635060006aab416",
        "hasResult": 'true',
        "authGroupId": -1

    }
    re = session.post(url_push, headers = header, data = json.dumps(data_push), timeout = 20)
    print(' push data ' + str(re.text))

    #邮件通知系统
    email_from = "12345@qq.com"             # 改为自己的发送邮箱
    email_to = email                        # 接收邮箱
    hostname = "smtp.qq.com"                # 不变，QQ邮箱的smtp服务器地址
    login = "12345"                         # 发送邮箱的用户名
    password = "12345343df"                 # 发送邮箱的密码，即开启smtp服务得到的授权码。注：不是QQ密码。
    subject = format_date_1 + '健康填报通知'  # 邮件主题
    text = (' push data ' + str(re.text))   # 邮件正文内容

    smtp = SMTP_SSL(hostname)               # SMTP_SSL默认使用465端口
    smtp.login(login, password)

    msg = MIMEText(text, "plain", "utf-8")
    msg["Subject"] = Header(subject, "utf-8")
    msg["from"] = email_from
    msg["to"] = email_to

    smtp.sendmail(email_from, email_to, msg.as_string())
    smtp.quit()
    print("健康填报邮件通知已发送")
