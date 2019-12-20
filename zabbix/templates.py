#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import json

class Template:
    def __init__(self, url, token, headers):
        self.url = url
        self.token = token
        self.headers = headers

    def getTempleteId(self, templates:list):
        ret = {}

        data = {
            "jsonrpc": "2.0",
            "method": "template.get",
            "params": {
                "output": "extend",
                "filter": {
                    "host": [
                        x for x in templates
                    ]
                }
            },
            "auth": self.token,
            "id": 1
        }
        res = requests.post(self.url, data=json.dumps(data), headers=self.headers)


        if res.json().get('result'):
            ret["code"] = 1
            ret["data"] = []
            tids = []
            tid = {}
            for t in res.json().get('result'):
                tids.append(t['templateid'])
            tid["tids"] = tids
            ret["data"].append(tid)
            return ret

        else:
            ret["code"] = 0
            ret["data"] = []
            return ret
