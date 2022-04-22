# -*- coding: utf-8 -*-

"""
@created on 2022/03/26
@author Yao Li
"""

class LOG(object):
    
    @staticmethod
    def info(msg):
        print("INFO: " + msg)

    @staticmethod
    def error(msg):
        print("ERROR: " + msg)
