'''
File       : baidu_img.py
Copyright  : ZhangKe
Date       : 2020-03-17
Desc       :
'''

import requests
import re
import os
import time

url = "http://image.baidu.com/search/acjson?tn=resultjson_com" \
      "&ipn=rj&ct=201326592&is=&fp=result&queryWord=737&cl=2&lm=-1" \
      "&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=" \
      "&word=737&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1" \
      "&fr=&expermode=&force=&pn={}&rn=30&gsm=1e&1584439032688="

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/80.0.3987.132 Safari/537.36"
}

for num in range(0, 4):
    pn = num * 30
    first_url = url.format(pn)
    res = requests.get(first_url, headers=headers)
    img_data = res.text
    img_url = re.findall(r'"thumbURL":"(.*?)"',img_data)
    print(img_url)

    baiduimg = "img"+str(num)

    if not os.path.exists(baiduimg):
        os.mkdir(baiduimg)

    for index, img_urls in enumerate(img_url):
        img_datas = requests.get(img_urls,headers=headers).content
        img_name = baiduimg+'/'+'%s.%s' % (index, img_urls.split('.')[-1])

        with open(img_name, 'wb') as f:
            f.write(img_datas)

    time.sleep(0.5)