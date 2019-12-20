#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import json

class login:
    def __init__(self, url, username, password, headers):
        self.url = url
        self.headers = headers
        self.username = username
        self.password = password

    def getToken(self):

        ret = {}

        data = {
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": self.username,
                "password": self.password
            },
            "id": 1,
            "auth": None,
        }


        res = requests.post(self.url, data=json.dumps(data), headers=self.headers)

        if res.json().get('result'):
            token = res.json().get('result')
            ret["code"] = 1
            ret["data"] = []
            tok = {}
            tok["token"] = token
            ret["data"].append(tok)
            return ret
        else:
            ret["code"] = 0
            ret["data"] = []
            return ret

