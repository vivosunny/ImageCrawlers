#500px.com scrap pictures 
import requests

class Login(object):
    def __init__(self):
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'location=CN; device_uuid=27510eb4-733c-456e-9f8a-9c1404b36794; _vwo_uuid_v2=D22D9E6F60A8C57C1F38D6DA291E60E1C|4a1933fe8fdb483ab6d55b1991fc2d94; amplitude_id500px.com=eyJkZXZpY2VJZCI6ImE1YmQ4ZjU4LTlhMTEtNDQ2Ni1iMWRiLTJiODVkZWI1MzhmYVIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTUzNTUyOTg2NDc2MiwibGFzdEV2ZW50VGltZSI6MTUzNTUyOTg2ODczNSwiZXZlbnRJZCI6MiwiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjJ9; _hpx1=BAh7DEkiD3Nlc3Npb25faWQGOgZFVEkiJWEyMWUzNmJmM2I0NThmMjViZDA3MmFjOTU5NzEzOWY3BjsAVEkiCWhvc3QGOwBGIg41MDBweC5jb21JIhl1c2Vfb25ib2FyZGluZ19tb2RhbAY7AEZUSSIYc3VwZXJfc2VjcmV0X3BpeDNscwY7AEZGSSIQX2NzcmZfdG9rZW4GOwBGSSIxRmZQNkVMVEQrT3MrYkhTeFNVcjJ3ZjlLSURBM0xQME1XeEczcEs1alhjTT0GOwBGSSIbcHJldmlvdXNfcGFnZV9yZWNvcmRlZAY7AEZUSSIccmVkaXJlY3Rpb25fYWZ0ZXJfbG9naW4GOwBGIhdodHRwczovLzUwMHB4LmNvbS8%3D--5baab2ab9dcec274181c7b5265c6e86f9c75ca7e; dmxRegion=false; _dm_sync=true',
            'Host': '500px.com',
            'If-None-Match': 'W/"db135feb4644edc1bbae0afef21078c8"',
            'Referer': 'https://500px.com/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3514.0 Safari/537.36'
        }
        self.login_url = 'https://500px.com/login'
        self.post_url = 'https://api.500px.com/v1/session'
        self.search_url = 'https://500px.com/search'
        self.session = requests.Session()
        
    def 
