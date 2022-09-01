"""
--*-- coding: utf-8 --*--
@Project ：spiderdemo 
@File    ：kgj.py
@IDE     ：PyCharm 
@Author  ：B6-72csh
@Date    ：2022/8/26 9:17
"""
import requests
import execjs
import json

base_url = 'https://service.kaogujia.com/api/sku/search?sort=0&sort_field=sales&limit=50&page=1'

headers = {
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJjWkhEaHJZMFB4YXdmbXRhT3VBIiwic2lkIjoiNTQ2Njk2NyIsImF1ZCI6IjEwMDAiLCJpc3MiOiJrYW9ndWppYS5jb20iLCJ0eXAiOiIxIiwibmJmIjoxNjYxNzU0MTc0LCJleHAiOjE2NjIzNTg5NzQsImlhdCI6MTY2MTc1NDE3NH0.UqzML08iGiVhrcNoX0AQBYO-4wGU11Mzk_M8jYxYbqo',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
params = {
    "keyword": "",
    "period": 3
}

response = requests.post(url=base_url, headers=headers, json=params).json()
data = response['data']['result']
with open('kgj_crypt.js', 'r', encoding='utf-8') as f:
    kgj_crypt_js = f.read()
decrypt_data = execjs.compile(kgj_crypt_js).call('_0x59bfc9', '/api/sku/search', data)
with open('data.json', 'a', encoding='utf-8') as f:
    json.dump(json.loads(decrypt_data), f, ensure_ascii=False, indent=4)
print(decrypt_data)
