import requests
import execjs

session = requests.Session()

with open("medium_9.js", "r") as f:
    js_code = f.read()

ctx = execjs.compile(js_code)
sign = ctx.call("get_cookie").split('=')[1].split(';')[0]

answer = ctx.call("get_answer").split('=')[1].split(';')[0]
print(answer)
cookies = {
    'sessionid': 'zgo7f7isq8l57qexdsfuc39t3y6t6v1i',
    'sign': sign,
}

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
}

response = session.get('https://www.python-spider.com/challenge/9', cookies=cookies, headers=headers)
# print(response.text)

data = {
    'anw': answer,
    'id': 9
}

resp = session.post('https://www.python-spider.com/challenge/api/check', cookies=cookies, data=data, verify=False)
print(resp.text)
