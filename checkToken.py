#!/usr/bin/python
# Env: python3
# Author: afei00123
# -*- coding: utf8 -*-

import os, time
from getToken import get_token

class check_Token():
    def check_token(self):
        if not os.path.isfile("access_token.txt"):
            print("[-] 检测到不存在access_token.txt，正在登录...")
            getToken = get_token()
            getToken.login("https://api.zoomeye.org/user/login")
            time.sleep(2)
            if not os.path.isfile("access_token.txt"):
                print("[-] 请求超时，请确认API是否可用！")
            else:
                with open("access_token.txt", "r") as fr:
                    token = fr.readline()
                    return token
        else:
            try:
                with open("access_token.txt", "r") as fr:
                    token = fr.readline()
                    return token
            except Exception as e:
                print("[-] access_token.txt中token失效！正在重新登录...")
                os.remove("access_token.txt")
                getToken = get_token()
                getToken.login("https://api.zoomeye.org/user/login")
                time.sleep(2)
                if not os.path.isfile("access_token.txt"):
                    print("[-] 请求超时，请确认API是否可用！")
                else:
                    with open("access_token.txt", "r") as fr:
                        token = fr.readline()
                        return token