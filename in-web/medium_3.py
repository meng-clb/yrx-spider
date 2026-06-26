import requests
import execjs
from urllib3.util import url

with open('medium_3.js', 'r') as f:
    js_code = f.read()

ctx = execjs.compile(js_code)
# cookie_m = ctx.call('get_cookie')
#
# cookies = {
#     'sessionid': 'fflurfvle4i6tw0r4coejydgtoblwjo3',
#     'm': str(cookie_m),
# }

headers = {
    'Referer': 'https://www.python-spider.com/challenge/3',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}



data = {
    'page': '1',
}


def sum_total(headers={}, client=requests, verify=False):
    """
    可以获取到数据之后，批量获取数据，并进行计算total
    :param url: 题目的url
    :param cookies: 题目需要用到的cookies
    :param headers: 请求头
    :param client: 请求方式 （requests，session）
    :return: total 计算的总和
    """
    total = 0
    for i in range(1, 101):
        cookie_m = ctx.call('get_cookie')

        cookies = {
            'sessionid': 'fflurfvle4i6tw0r4coejydgtoblwjo3',
            'm': str(cookie_m),
        }

        data = {
            'page': str(i),
        }
        print(f'=========== 第{i}页 ===========')
        resp = requests.post('https://www.python-spider.com/api/challenge3', cookies=cookies, headers=headers,
                             data=data, verify=False)
        re = resp.json()['data']
        for r in re:
            total += int(r['value'])
            print(r['value'])
    return total


# resp = requests.post('https://www.python-spider.com/api/challenge3', cookies=cookies, headers=headers, data=data,verify=False)
# print(resp.json())
total = sum_total( headers=headers, client=requests, verify=False)
print(total)

data = {
    'anw': total,
    'id': 3
}

cookie_m = ctx.call('get_cookie')

cookies = {
    'sessionid': 'fflurfvle4i6tw0r4coejydgtoblwjo3',
    'm': str(cookie_m),
}
resp = requests.post('https://www.python-spider.com/challenge/api/check', cookies=cookies, data=data,
                       verify=False)

print(resp.json())