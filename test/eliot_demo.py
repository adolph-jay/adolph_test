# -*- coding: utf-8 -*-
# @Time    : 2020/7/3 15:43
# @Author  : Adolph
# @Email   : gaojie@ti-net.com.cn
# @File    : eliot_demo.py
# @Software: PyCharm
# @Product : Clink2 OpenApi
# @Company : Tinet

import eliot

import requests
from eliot import start_action, to_file

# 1. to_file
to_file(open("linkcheck.log", "w"))


def check_links(urls):
    with start_action(action_type="check_links", urls=urls):
        for url in urls:
            try:
                # 2. start_action
                with start_action(action_type="download", url=url):
                    response = requests.get(url)
                    response.raise_for_status()
            except Exception as e:
                raise ValueError(str(e))

try:
    check_links(["http://eliot.readthedocs.io", "http://nosuchurl"])
except ValueError:
    print("Not all links were valid.")