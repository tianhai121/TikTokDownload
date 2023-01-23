#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import re
import sys
import json
import Util
import getopt
import requests
from datetime import date

# from retrying import retry

def find_key(string):
    key_modal = re.findall(
        'modal_id=\d+', string
    )
    key = key_modal[0].split("=")[-1]
    return key


def get_video_url(url, headers):
    key = find_key(url)
    jx_url = f'https://www.iesdouyin.com/aweme/v1/web/aweme/detail/?aweme_id=' \
             f'{key}&aid=1128&version_name=23.5.0&device_platform=android&os_version=2333'
    js = json.loads(requests.get(url=jx_url, headers=headers).text)
    video_title_init = str(js['aweme_detail']['desc'])
    video_title = video_title_init.replace(' ','-')
    video_title = video_title.replace('/','-')
    try:
        video_url = str(
            js['aweme_detail']['video']['play_addr']
            ['url_list'][2]
        )  # .replace('playwm', 'play')  # 去水印后链接
    except:
        print('[  提示  ]:视频链接获取失败\r')
        video_url = ''
    return video_url,video_title


# @retry(stop_max_attempt_number=3)
def download():
    # 视频下载
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, '
                      'like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.66',
        'Cookie': 'msToken=%s' % Util.generate_random_str(107)
    }
    video_url,video_title = get_video_url(url, headers)
    r = requests.get(url=video_url, headers=headers)
    # 创建用户文件夹
    video_path = "./Download-{}/".format(date.today())
    if not Util.os.path.exists(video_path):
        Util.os.makedirs(video_path)
    if not Util.Status_Code(r.status_code):
        with open(video_path+f'{video_title}.mp4', 'wb') as f:
            f.write(r.content)
            print('[  视频  ]:%s.mp4 下载完成\r' % video_title)
    else:
        print("{}视屏下载失败".format(date.today()))


if __name__ == "__main__":
    # url必须含有modal_id=7188329661133262084
    url = "https://www.douyin.com/user/MS4wLjABAAAA4l9MvOQWBwMp1LW2UlD1ZR5D3Dcn7ipC1mTb7uuz_5g?modal_id=7188329661133262084"
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, '
                      'like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.66',
        'Cookie': 'msToken=%s' % Util.generate_random_str(107)
    }
    download()
