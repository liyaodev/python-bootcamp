# -*- coding: utf-8 -*-

"""
@created on 2022/03/26
@author Yao Li
"""

import json
import ctypes
from ctypes import c_float
from common.logger import LOG

class C_Type(object):
    
    def __init__(self) -> None:
        self.so = ctypes.CDLL('widget/ctype/lib/sum.so')
    
    def predict(self, req_dict={}):
        LOG.info("this is ctype infer, req_dict=%s" % json.dumps(req_dict))
        a, b = req_dict.get("a", 50), req_dict.get("b", 100)
        sum_val = self.so.sum(a)
        add_val = self.so.add(c_float(a), c_float(b))
        LOG.info("so.sum(%d) = %d" % (a, sum_val))
        LOG.info("so.add(%d, %d) = %d" % (a, b, add_val))
        req_dict["sum"] = sum_val
        req_dict["add"] = add_val
        return req_dict

    def version(self):
        return '20220326'


def get_plugin_class():
    return C_Type
