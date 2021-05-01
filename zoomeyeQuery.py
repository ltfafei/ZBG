#!/usr/bin/python
# Env: python3
# Author: afei00123
# -*- coding: utf8 -*-

import requests, json, argparse
from colorama import init
init(autoreset=True)
from checkToken import check_Token
from getToken import get_token

def title():
    print("")
    print('*'.center(60, '*'))
    print("Version：zoomeye_Batch_get v1.0".center(50))
    print("github：https://github.com/ltfafei".center(50))
    print("CSDN: afei00123.blog.csdn.net".center(50))
    print("公众号：网络运维渗透".center(40))
    print("")
    print('*'.center(60, '*'))
    print("")

class get_Query():
    def query(self, query, page, num, facet, file):
        gettoken = check_Token()
        random_ua = get_token()
        headers = {
            'Authorization': "JWT " +gettoken.check_token(),
            "User-Agent": random_ua.random_useragent()
        }
        api = "https://api.zoomeye.org/host/search"
        index = 0

        while True:
            try:
                #如果index=设置的最大页数，则跳出循环
                if index == num:
                    break
                print(f"\033[31m[+] 正在获取第{page}页结果：")
                page += 1
                index += 1
                query_res = requests.get(api, headers=headers, params={"query": query, "page": page, "facets": facet}).text
                # 转化为json，方便提取字段
                json_res = json.loads(query_res)["matches"]
                count = 1
                for i in json_res:
                    print(f"[{count}] " + i['ip'] + ":" + str(i['portinfo']['port']))
                    res = i['ip'] + ":" + str(i['portinfo']['port'])
                    with open(file, "a") as fw:
                        fw.writelines(res + "\n")
                    count += 1
            except Exception as e:
                print("[-] 请确认是否达到最大查询次数！")

if(__name__ == '__main__'):
    title()
    parser = argparse.ArgumentParser(description="Zoomeye batch gather tools")
    parser.add_argument(
        '-q', '--query',
        metavar='', required=True, type=str,
        help='Please input query argument. eg: shiro'
    )
    parser.add_argument(
        '-p', '--page',
        metavar='', required=False, type=int, default=1,
        help='Please input start page. eg: 2'
    )
    parser.add_argument(
        '-n', '--num',
        metavar='',required=False, type=int, default=1,
        help='Please input max page. eg: 2'
    )
    parser.add_argument(
        '-F', '--facet',
        metavar='', type=str, required=False,
        help='Please input covariance item. eg: server'
    )
    parser.add_argument(
        '-o', '--file', required=False,
        metavar='', type=str, default='output.txt',
        help='Please input output file path. eg: output.txt'
    )
    args = parser.parse_args()
    run_ZBG = get_Query()
    run_ZBG.query(args.query, args.page, args.num, args.facet, args.file)
    pass