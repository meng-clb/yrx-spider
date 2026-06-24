import requests

session = requests.Session()

cookies = {
    'sessionid': 'q3pnnguy5uhw15sdze8kscwclnob5yqs'
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.python-spider.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.python-spider.com/challenge/6',
    'sec-ch-ua': '"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'sessionid=q3pnnguy5uhw15sdze8kscwclnob5yqs; sign=sxhbwmcqpa',
}



sum = 0
for i in range(1,101):
    data = {
        'page': str(i),
    }
    print(f'=========== 第{i}页 ===========')
    resp = session.post('https://www.python-spider.com/api/challenge6', cookies=cookies, headers=headers, data=data)
    re = resp.json()['data']
    for r in re:
        sum += int(r['value'])
        print(r['value'])

print(sum)
"""
获取到数据之后，计算完毕，提交数据
"""
data = {
    'anw':sum,
    'id':6
}
resp = session.post('https://www.python-spider.com/challenge/api/check', cookies=cookies, headers=headers,data=data)

print(resp.json())
