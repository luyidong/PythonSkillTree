# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: mango
@contact: w4n9@sina.com
@create: 16/7/4
hail hydra!
"""

__author__ = "mango"
__version__ = "0.1"


import rpyc


client = rpyc.connect("127.0.0.1", 18861)
client.root.get_answer()
client.root.question()
