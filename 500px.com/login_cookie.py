#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author:Xiari

import requests
import os
#login_500px.com
#def ligin_cookie():
headers = {
    'Cookies': '_srt=BAhJIhYyOTQ3MTIyOTp6RGgwYWc9PQY6BkVU--1978abcd7bc07763af744983a1c61dc70e5e17f6; device_uuid=2091cb10-b9c2-4f8b-abaa-eb6f88e4a0f1; _vwo_uuid_v2=D86DF2764A615D65968EDA6804E946E4F|b538ff18dcf14b2b552868bdc585da55; __hstc=133410001.9d774c484c77234c686e036e86d57848.1534662345484.1534662345484.1534662345484.1; __hssrc=1; __hssc=133410001.1.1534662345484; hubspotutk=9d774c484c77234c686e036e86d57848; remember_user_token=BAhbB1sGaQT9scEBSSIiJDJhJDEwJFZzb2VrVkV6Q1pVMUphNURjUzFIY08GOgZFVA%3D%3D--75488ba2aca367c05fec51a57c85f07a2ec9b2d3; locale=zh-CN; ab.storage.userId.46204105-396b-449a-9da2-1df53cd8a2a8=%7B%22g%22%3A%2229471229%22%2C%22c%22%3A1534662449543%2C%22l%22%3A1534662449543%7D; ab.storage.deviceId.46204105-396b-449a-9da2-1df53cd8a2a8=%7B%22g%22%3A%22c3e06bf8-77f3-4dd7-cc28-a7ae5e22d68c%22%2C%22c%22%3A1534662449545%2C%22l%22%3A1534662449545%7D; _hpx1=BAh7DUkiD3Nlc3Npb25faWQGOgZFVEkiJTU4ODFmYjY4OTE0ZmJlMTRiNmUwZDA2OTU4YjlhZGYyBjsAVEkiCWhvc3QGOwBGIhJhcGkuNTAwcHguY29tSSIQX2NzcmZfdG9rZW4GOwBGSSIxZ21td2tOLzBZTEQ2U3NvazR1dVd4SHhwcG9FMWlyZDZYajBXamVFMG16ST0GOwBGSSIZdXNlX29uYm9hcmRpbmdfbW9kYWwGOwBGVEkiGHN1cGVyX3NlY3JldF9waXgzbHMGOwBGRkkiGXdhcmRlbi51c2VyLnVzZXIua2V5BjsAVFsHWwZpBP2xwQFJIiIkMmEkMTAkVnNvZWtWRXpDWlUxSmE1RGNTMUhjTwY7AFRJIglfc3J0BjsARkkiFjI5NDcxMjI5OnpEaDBhZz09BjsAVEkiEXByZXZpb3VzX3VybAY7AEZJIjsvc2VhcmNoP3N1Ym1pdD1TdWJtaXQmcT0lRTQlQkElQkElRTUlODMlOEYmdHlwZT1waG90b3MGOwBU--1726f2705450d449a29ed88b7fc375c2af5d4c96; amplitude_id500px.com=eyJkZXZpY2VJZCI6ImJjNTViZjExLWEyMGUtNDY0YS1iYzYyLTdhMjY4ZWM4NjQ2YVIiLCJ1c2VySWQiOiIyOTQ3MTIyOSIsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTUzNDY2MjMyNzk0NywibGFzdEV2ZW50VGltZSI6MTUzNDY2MzYzNjQyNiwiZXZlbnRJZCI6MSwiaWRlbnRpZnlJZCI6NCwic2VxdWVuY2VOdW1iZXIiOjV9; ab.storage.sessionId.46204105-396b-449a-9da2-1df53cd8a2a8=%7B%22g%22%3A%22a5de0b13-0bb4-6d19-f372-4d20b9fcb3b6%22%2C%22e%22%3A1534665436448%2C%22c%22%3A1534662449543%2C%22l%22%3A1534663636448%7D',
    #'Cookies': 'location=CN; device_uuid=8c0f76dc-8ecd-40d0-bcc7-570d33d60355; _dm_sync=true; dmxRegion=false; _vwo_uuid_v2=DE95501343244812179BA3F407FD03419|3bfd7f6c83e350dd503fe0233f4cb6d2; fb_invalid_token_dismissed=true; hide_site_promotion_banner=sunset_2018; amplitude_id500px.com=eyJkZXZpY2VJZCI6IjQ1MTliYjg5LWY4MjktNDAzMi1iY2RmLTA0Nzc1ZGIzZTYzZVIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTUzNDY0MjExMTc5MCwibGFzdEV2ZW50VGltZSI6MTUzNDY0MzU4Njg4MiwiZXZlbnRJZCI6MCwiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjB9; _srt=BAhJIhYyOTQ3MTIyOTp6RGgwYWc9PQY6BkVU--1978abcd7bc07763af744983a1c61dc70e5e17f6; remember_user_token=BAhbB1sGaQT9scEBSSIiJDJhJDEwJFZzb2VrVkV6Q1pVMUphNURjUzFIY08GOgZFVA%3D%3D--75488ba2aca367c05fec51a57c85f07a2ec9b2d3; _hpx1=BAh7DkkiD3Nlc3Npb25faWQGOgZFVEkiJTcxNjRkNWFhN2M2NzE4NzM0YWM1OTc1M2JjZDU1ZmQwBjsAVEkiCWhvc3QGOwBGIhJhcGkuNTAwcHguY29tSSIZdXNlX29uYm9hcmRpbmdfbW9kYWwGOwBGVEkiGHN1cGVyX3NlY3JldF9waXgzbHMGOwBGRkkiEF9jc3JmX3Rva2VuBjsARkkiMVRqcnErblphZWhRYzFUcmUzQWJJbjlxU3NYeWxKcDBKNlRNbVRBY0JvcWc9BjsARkkiG3ByZXZpb3VzX3BhZ2VfcmVjb3JkZWQGOwBGVEkiHHJlZGlyZWN0aW9uX2FmdGVyX2xvZ2luBjsARkkiDC9zZWFyY2gGOwBUSSIZd2FyZGVuLnVzZXIudXNlci5rZXkGOwBUWwdbBmkE%2FbHBAUkiIiQyYSQxMCRWc29la1ZFekNaVTFKYTVEY1MxSGNPBjsAVEkiCV9zcnQGOwBGSSIWMjk0NzEyMjk6ekRoMGFnPT0GOwBU--3490a25c753bc48e4fe729ee1bde0f1351df32be',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Host': '500px.com',
    'Referer': 'https://500px.com/login',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3514.0 Safari/537.36',
}
session = requests.Session()
url = 'https://500px.com/'
html = session.get(url, headers = headers)

'''
params = {
    #'field email unified_signup__input': email,
    #'field password unified_signup__input': password,
    #'button submit medium full unified_signup__submit_button': '登录',
    
    'session[email]': 'vivosunny@dawin.com',
    'session[password]': 'vivosunny',
    'authenticity_token': '/icQ8kjLQVhWTqKJbGwQOGLqSbL5f62jouWupWSoPHF8TqBilz8h6KwEaK2Oh4b8HoPvM8z1Gtn82LgohZynQw==',
}
session_url = 'https://api.500px.com/v1/session'
session_html = requests.post(session_url, data = params)
'''
#print(html.text)

with open('C:\\Users\\Administrator\\PycharmProjects\\TestPython\\500pxCrawler\\login_cookie.txt', 'w', encoding='utf-8') as f:
    f.write(html.text)
