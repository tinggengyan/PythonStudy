#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

branchName = raw_input("please input branch name to be checkout ")

os.system("git checkout -b " + branchName + " origin/" + branchName)
os.chdir("repos")

for x in os.listdir('.'):
    if os.path.isdir(x):
        os.chdir(x)
        os.system("git checkout -b " + branchName + " origin/" + branchName)
        os.chdir("..")
