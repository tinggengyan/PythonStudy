#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
import platform
import subprocess


class CheckHelper(object):
    def checkout(self):
        currentDir = os.getcwd()
        print currentDir  # 打印当前目录


checker = CheckHelper()
checker.checkout()
