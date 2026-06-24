from wsgiref import headers

import requests
from requests import session


def sum_total(url, cookies, headers={}, client=requests, verify=False):
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
        data = {
            'page': str(i),
        }
        print(f'=========== 第{i}页 ===========')
        if client == session:
            resp = client.post(url=url, cookies=cookies, data=data, verify=verify)
        elif client == requests:
            resp = client.post(url=url, data=data, cookies=cookies, headers=headers, verify=verify)
        re = resp.json()['data']
        for r in re:
            total += int(r['value'])
            print(r['value'])
    return total


def answer(total, cookies, id, headers={}, client=requests, verify=False):
    """
    获取到数据之后，计算完毕，提交数据
    """
    data = {
        'anw': total,
        'id': id
    }

    if client == session:
        resp = client.post('https://www.python-spider.com/challenge/api/check', cookies=cookies, data=data,
                           verify=verify)
    else:
        resp = client.post('https://www.python-spider.com/challenge/api/check', cookies=cookies, headers=headers,
                           data=data, verify=verify)

    print(resp.json())
