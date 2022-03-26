# -*- coding: utf-8 -*-

"""
@created on 2022/03/26
@author Yao Li
"""

class PluginException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
