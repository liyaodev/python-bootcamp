# -*- coding: utf-8 -*-

"""
@created on 2022/03/26
@author Yao Li
"""

import json
from common.logger import LOG

class Demo(object):
    
    # def __init__(self) -> None:
    #     pass
    
    def predict(self, req_dict={}):
        LOG.info("this is demo infer, req_dict=%s" % json.dumps(req_dict))
        return req_dict

    def version(self):
        return '20220326'


def get_plugin_class():
    return Demo

