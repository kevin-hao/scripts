#!/usr/bin/env python
# -*- coding:utf-8 -*-


from scripts.zabbix.Login import login
from scripts.zabbix.templates import Template
from scripts.zabbix.hostgroup import HostGroup
from scripts.zabbix.host import Host
from scripts.zabbix.config import Config


if __name__ == '__main__':

    url = Config.zabbixApi
    username = Config.zabbixUsername
    password = Config.zabbixPassword

    headers = {
        'Content-Type': 'application/json-rpc'
    }

    # 获取token
    tk = login(url, username, password, headers)
    token = ""
    if tk.getToken().get('code'):
        token = tk.getToken().get('data')[0]['token']
    else:
        token = tk.getToken().get('token')
        exit("用户名或密码错误")

    # 获取模版id
    templates = ["Template OS Linux", "Template App Zabbix Server"]
    tempIds = []
    template = Template(url=url, headers=headers, token=token)
    tids = template.getTempleteId(templates)
    if tids.get('code'):
        tempIds = tids.get('data')[0]['tids']
    else:
        exit("模版不存在")


    # 获取主机组id
    groupName = ["Zabbix servers", "Linux servers"]
    hostgroup = HostGroup(url=url, headers=headers, token=token)
    gids = hostgroup.getHostGroupId(groupName)
    grouIds = []
    if gids.get('code'):
        grouIds = gids.get('data')[0]['gids']
    else:
        exit("主机组不存在")

    """添加监控主机"""
    hosts = "10.0.1.10"
    add_host = Host(url=url, headers=headers, token=token)
    ret = add_host.AddHost(host=hosts, templateId=tids, hostGroupId=grouIds)
    if ret.get('code'):
        exit(ret.get('data')[0]['result'])
    else:
        exit(ret.get('data')[0]['result'])




