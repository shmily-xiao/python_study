#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

if __name__ == '__main__':
    string = r"[;]?wwwwww@34\.cn"
    need_string = "Bwwwwww@34.cn;wwwwwww@34.cn;wwwwww@34.cn"
    rec = re.compile(string)
    print rec.findall(need_string)