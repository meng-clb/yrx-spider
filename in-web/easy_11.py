from re import match

import requests
import execjs
from bs4 import BeautifulSoup
from answer_post import answer

session = requests.Session()
cookies = {
    'sessionid': 'zgo7f7isq8l57qexdsfuc39t3y6t6v1i',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://www.python-spider.com/challenge/11',
    'sec-ch-ua': '"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
    # 'cookie': 'sessionid=zgo7f7isq8l57qexdsfuc39t3y6t6v1i; __jsl_clearance=1782710282.869|0|clD4VpfqhdaLBWywKWy%2FZyfi6d_5aea5d8c6d1ac0b7f1722053a135c7143D',
}

response = session.get('https://www.python-spider.com/challenge/11', cookies=cookies, headers=headers)
# print(response.text)
jscode = match(r"<script>(.*)</script>", response.text).group(1)

with open('./easy_11.js', 'r') as f:
    js = f.read()

ctx = execjs.compile(js.replace('__jscode', jscode))
cookie = ctx.call('decode').split('=')[1].split(';')[0]
# print(cookie)

cookies = {
    'sessionid': 'zgo7f7isq8l57qexdsfuc39t3y6t6v1i',
    '__jsl_clearance': cookie
}
response = session.get('https://www.python-spider.com/challenge/11', cookies=cookies, headers=headers)
# print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
data = soup.find('tr')
total = 0
for tr in data.find_all('td'):
    total += int(tr.text)
# print(data)


answer(total, cookies, id=11, client=session)

