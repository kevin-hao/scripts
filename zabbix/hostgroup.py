#!/usr/bin/env python
# -*- coding:utf-8 -*-


import requests
import json


class HostGroup:
    def __init__(self,url, token, headers):
        self.url = url
        self.token = token
        self.headers = headers

    def getHostGroupId(self, groupName:list):
        ret = {}
        data = {
            "jsonrpc": "2.0",
            "method": "hostgroup.get",
            "params": {
                "output": "extend",
                "filter": {
                    "name": [
                        hostGroup for hostGroup in groupName
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
            gids = []
            gid = {}
            for g in res.json().get('result'):
                gids.append(g['groupid'])
            gid["gids"] = gids
            ret["data"].append(gid)
            return ret
        else:
            ret["code"] = 0
            ret["data"] = []
            return ret