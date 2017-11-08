# coding: utf-8
import os
import requests
import json

workspace = "D:\workspace\workCode"
os.chdir(workspace)

url = "http://10.200.5.103/api/v3/groups/android_lvmm/projects"
ra = {"per_page": 50, "private_token": "qSyy1Y8eNgPX2SxW_gyG"}


def getModuleName(url):
    split = url.split("/")
    moduleGit = split[len(split) - 1].split(".")
    return moduleGit[0]


content = requests.get(url, params=ra)
groupProjects = json.loads(content.content)

# clone the main app
listdir = os.listdir('.')
if "combine" not in listdir:
    mainRepo = "http://10.200.5.103/android_lvmm/combine.git"
    os.system("git clone " + mainRepo)
# clone the sub modules
os.chdir("combine")
os.chdir("repos")
listdir = os.listdir('.')

for a in groupProjects:
    httpUrl = a["http_url_to_repo"]
    sshUrl = a["ssh_url_to_repo"]
    # 可以在此切换协议
    if "combine" not in httpUrl:
        if getModuleName(httpUrl) not in listdir:
            os.system("git clone " + httpUrl)
