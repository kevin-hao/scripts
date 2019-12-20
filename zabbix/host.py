#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import json

class Host:

    def __init__(self, url, token, headers):

        self.url = url
        self.token = token
        self.headers = headers

    def AddHost(self, host, templateId: list, hostGroupId: list):

        ret = {}
        data = {
            "jsonrpc": "2.0",
            "method": "host.create",
            "params": {
                "host": host,
                "interfaces": [
                    {
                        "type": 1,
                        "main": 1,
                        "useip": 1,
                        "ip": host,
                        "dns": "",
                        "port": "10050"
                    }
                ],
                "groups": hostGroupId,
                "templates": templateId
            },
            "auth": self.token,
            "id": 1
        }

        res = requests.post(self.url, data=json.dumps(data),headers=self.headers)
        if res.json().get('result'):
            ret["code"] = 1
            ret["data"] = []
            ret["data"].append({"result": "添加成功"})
            return ret
        else:
            ret["code"] = 0
            ret["data"] = [res.json().get('error')]
            return ret