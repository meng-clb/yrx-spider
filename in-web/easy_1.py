import time
import base64
import hashlib
from answer_post import answer


def get_token():
    a = '9622'

    # 对应 JS: String(Date.parse(new Date()) / 1000)
    timestamp = str(int(time.time()))

    # 对应 JS: window.btoa(a + timestamp)
    btoa_str = base64.b64encode((a + timestamp).encode('utf-8')).decode('utf-8')

    # 对应 JS: hex_md5(...)
    tokens = hashlib.md5(btoa_str.encode('utf-8')).hexdigest()
    return timestamp, tokens


import requests

cookies = {
    'sessionid': 'q3pnnguy5uhw15sdze8kscwclnob5yqs',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://www.python-spider.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.python-spider.com/challenge/1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'safe': get_token()[1],
    'sec-ch-ua': '"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'timestamp': get_token()[0],
}

# data = {
#     'page': '5',
# }

# resp = requests.post('https://www.python-spider.com/api/challenge1', cookies=cookies, headers=headers, data=data, verify=False)
#
# print(resp.json())
# print(get_token())

total = 0
for i in range(1, 101):
    headers['timestamp'] = get_token()[0]
    headers['safe'] = get_token()[1]
    data = {
        'page': str(i),
    }
    print(f'=========== 第{i}页 ===========')
    resp = requests.post('https://www.python-spider.com/api/challenge1', cookies=cookies, headers=headers, data=data,
                         verify=False)
    re = resp.json()['data']
    for r in re:
        total += int(r['value'])
        print(r['value'])
print(total)

answer(total=total, cookies=cookies, id=1, headers=headers)
