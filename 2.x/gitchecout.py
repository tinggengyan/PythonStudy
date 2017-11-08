#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

workspace = "D:\workspace\workCode\combine"
os.chdir(workspace)

branchName = raw_input("please input branch name to be checkout ")

# 先切换当前主工程的分支
os.system("git checkout " + branchName)
os.chdir("repos")

for x in os.listdir('.'):
    if os.path.isdir(x):
        os.chdir(x)
        os.system("git checkout " + branchName)
        os.chdir("..")
