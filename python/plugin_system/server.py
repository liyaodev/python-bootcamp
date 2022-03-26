# -*- coding: utf-8 -*-

"""
@created on 2022/03/26
@author Yao Li
"""

import os
import sys
from os.path import dirname, abspath

BASE_DIR = dirname(abspath(__file__))
sys.path.insert(0, BASE_DIR)

from common.manager import PluginManager, PluginV2Manager


if __name__ == '__main__':

    # manager = PluginManager()
    manager = PluginV2Manager()
    # 验证单个插件
    plugin = manager.get_plugin("demo")
    plugin.predict({"plugin": "demo"})
    # 验证所有插件
    for name, plugin in manager.get_total_plugin().items():
        plugin.predict({"plugin": name})
    
