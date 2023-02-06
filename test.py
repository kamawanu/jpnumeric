#!/usr/bin/env python3
# !-*- coding:utf-8 -*-

import jpnumeric

TEST = [
    # "1234567890",
    "壱拾弐億参阡四百五拾六萬七阡八百九拾",
    "12億3456万7890",
    r"１２３４５６７８９０",
    "百万",
    "億千万",
    "闇物語 第壱拾参章",
    "数字ありません",
]

jpnumeric.to_int(u"百万")

for test1 in TEST:
    r = jpnumeric.replace_jpnumeric_int(test1)
    print (test1, r)
