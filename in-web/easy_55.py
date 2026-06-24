import json

import requests
from pathlib import Path
import subprocess
from answer_post import answer


def decrypt_by_node(encrypted_str):
    js_path = Path(__file__).with_name("easy_55.js")
    result = subprocess.run(["node", str(js_path), encrypted_str], capture_output=True, text=True)

    if result.returncode != 0:
        raise Exception(result.stderr)

    return result.stdout.strip()




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
    'Referer': 'https://www.python-spider.com/challenge/55',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    # 'Cookie': 'sessionid=q3pnnguy5uhw15sdze8kscwclnob5yqs',
}

total = 0
for i in range(1, 101):
    data = {
        'page': str(i),
    }
    print(f'=========== 第{i}页 ===========')
    resp = requests.post('https://www.python-spider.com/api/challenge55', cookies=cookies, headers=headers, data=data,
                         verify=False)
    encrypted_str = resp.json()['result']
    print(encrypted_str)

    plain_text = decrypt_by_node(encrypted_str)
    print(plain_text)
    re = json.loads(plain_text)['data']
    for r in re:
        total += int(r['value'])
        print(r['value'])
print(total)

answer(total=total, cookies=cookies, id=55, headers=headers)

# resp = requests.post('https://www.python-spider.com/api/challenge55', cookies=cookies, headers=headers, data=data,verify=False)
# print(resp.json())
# encrypted_str = resp.json()['result']
# plain_text = decrypt_by_node(encrypted_str)
#
# print(plain_text)
