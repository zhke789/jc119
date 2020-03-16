import requests
from lxml import etree
from prettytable import PrettyTable
import json

headers = {
    "Cookie": "JSESSIONID=5429B6A2642ACF7C700BE1A231FC516B",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36"
}

url = 'http://jc119.iok.la/flight/query/alljoindynflight'

res = requests.get(url, headers=headers).text

data = etree.HTML(res)

# result = data.xpath('//tr/td[@class="AIRLINES"]/text()')

# res = data.xpath('string(//tr)')
# df = pd.DataFrame(res.text)

#
#
# print(result)
# for i,item in enumerate(result):
#     print(i,item)

# # for i, a in enumerate(res):
# print(result)

table = data.xpath('//tr')

dep = []

for i in table:
    # id = "".join(i.xpath('./@id'))
    a1 = "".join(i.xpath('./td[@class="FEXD"]/text()'))  # 日期
    a2 = "".join(i.xpath('./td[@class="AIRLINES"]/text()'))  # 航线
    a3 = "".join(i.xpath('./td[@class="CRAFTTYPE"]/text()'))  # 机型
    a4 = "".join(i.xpath('./td[@class="CRAFTSITE"]/text()'))  # 机位
    a5 = "".join(i.xpath('./td[@class="PLANTAKEOFFTIME"]/text()'))  # 预达
    a6 = "".join(i.xpath('./td[@class="OFFIN"]/text()'))  # 进出

    print(*a1, *a2, *a3, *a4, *a5, *a6)

    # x = PrettyTable(["日期", "航线", "机型", "机位","预达","进出"])
    # x = PrettyTable(a1, a2, a3, a4, a5, a6)
    # print(x)

    # data = {"id": id,
    #         "日期": a1,
    #         "航线": a2,
    #         "机型": a3,
    #         "机位": a4,
    #         "预达": a5,
    #         "进出": a6
    #         }
    # js = json.dumps(data)
    # with open('data.txt', 'w', encoding='utf-8') as fp:
    #     fp.write(id, 'a1', 'a2')
    # print('下载成功！！！！')

# print(js)
