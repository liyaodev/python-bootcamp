# -*- coding: utf-8 -*-

"""
@created on 2022/03/26
@author Yao Li
"""

import os
from os.path import join, dirname, abspath
import json

import collections

from common.logger import LOG
from common.error import PluginException


class BaseManager(object):
    """插件管理基类"""
    
    def __init__(self) -> None:
        pass

    def get_plugin(self, name):
        """根据调用，返回插件实例"""
        raise RuntimeError('not implemented yet!')

    def get_total_plugin(self):
        """返回所有插件"""
        raise RuntimeError('not implemented yet!')


class PluginManager(BaseManager):
    """插件管理服务类"""

    def __init__(self):
        self.conf_dict = {}
        self.plugin_dict = collections.OrderedDict()
        
        with open(join(dirname(abspath(__file__)), "plugin.conf"), "r", encoding="utf-8") as f:
            self.conf_dict = json.load(f)
            
        # 初始化插件加载
        for key, plugin in self.conf_dict.items():
            self._load_plugin(key, plugin['infer_dir'])

        print(self.plugin_dict)

    def get_plugin(self, name, reload = False):
        if name not in self.conf_dict:
            raise PluginException("plugin \"%s\" not configured." % name)
        
        if name not in self.plugin_dict or reload:
            self._load_plugin(name, self.conf_dict['name']['infer_dir'])
        
        return self.plugin_dict.get(name)
    
    def get_total_plugin(self):
        return self.plugin_dict

    def _load_plugin(self, p_name, p_dir):
        """插件加载"""
        try:
            p = __import__(p_dir, fromlist=[p_name])
            clazz = p.get_plugin_class()
            o = clazz()
            self.plugin_dict.setdefault(p_name, o)
        except Exception as e:
            LOG.error("load plugin %s error: %s." % (p_name, str(e)))


class PluginV2Manager(PluginManager):
    """
        插件管理服务类
        优化项：去除配置文件
    """

    def __init__(self):
        self.conf_dict = {}
        self.plugin_dict = collections.OrderedDict()
        
        # 初始化插件加载
        widget_dir = join(dirname(dirname(abspath(__file__))), 'widget')
        widget_list = os.environ.get('WIDGET_LIST')     # 可支持配置加载指定插件
        widget_list = widget_list.split(',') if widget_list else os.listdir(widget_dir)
        for f_name in widget_list:
            path = os.path.join(widget_dir, f_name)
            if os.path.isdir(path) and os.path.exists(join(path, 'infer.py')):
                infer_dir = "widget." + f_name + '.infer'
                self._load_plugin(f_name, infer_dir)
                self.conf_dict[f_name] = {"infer_dir": infer_dir}
        
        print(self.plugin_dict)


class OtherManager(BaseManager):
    
    def get_plugin(self, name):
        """获取指定插件"""
        pass
    
    def get_total_plugin(self):
        """获取所有插件"""
        pass