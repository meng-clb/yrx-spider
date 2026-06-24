from collections import OrderedDict
from answer_post import answer
import requests

session = requests.Session()
session.verify = False
session.headers.clear()
cookies = {
    'sessionid': 'q3pnnguy5uhw15sdze8kscwclnob5yqs'
}

# resp = session.post('https://www.python-spider.com/api/challenge10', data=data, cookies=cookies)

total = 0
for i in range(1, 101):
    data = {
        'page': str(i),
    }
    body = f'page={i}'
    session.headers = OrderedDict([
        ('Content-Length', str(len(body.encode()))),
        ("Pragma", "no-cache"),
        ("Cache-Control", "no-cache"),
        ("sec-ch-ua-platform", "\"macOS\""),
        ("X-Requested-With", "XMLHttpRequest"),
        ("User-Agent",
         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"),
        ("Accept", "application/json, text/javascript, */*; q=0.01"),
        ("sec-ch-ua", "\"Google Chrome\";v=\"149\", \"Chromium\";v=\"149\", \"Not)A;Brand\";v=\"24\""),
        ("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8"),
        ("sec-ch-ua-mobile", "?0"),
        ("Origin", "https://www.python-spider.com"),
        ("Sec-Fetch-Site", "same-origin"),
        ("Sec-Fetch-Mode", "cors"),
        ("Sec-Fetch-Dest", "empty"),
        ("Referer", "https://www.python-spider.com/challenge/10"),
        ("Accept-Encoding", "gzip, deflate, br, zstd"),
        ("Accept-Language", "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"),
    ])

    print(f'=========== 第{i}页 ===========')
    resp = session.post('https://www.python-spider.com/api/challenge10', data=data, cookies=cookies)
    re = resp.json()['data']
    for r in re:
        total += int(r['value'])
        print(r['value'])

print(total)
"""
获取到数据之后，计算完毕，提交数据
"""
# data = {
#     'anw': total,
#     'id': 10
# }
# resp = session.post('https://www.python-spider.com/challenge/api/check', cookies=cookies, data=data)
#
# print(resp.json())

answer(total=total,cookies=cookies,id=10,client=session)