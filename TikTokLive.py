#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:TikTokLive.py
@Date       :2022/09/15 17:29:10
@Author     :JohnserfSeed
@version    :1.0
@License    :(C)Copyright 2019-2022, Liugroup-NLPR-CASIA
@Github     :https://github.com/johnserf-seed
@Mail       :johnserfseed@gmail.com
-------------------------------------------------
Change Log  :
-------------------------------------------------
'''
import Util

live_url = Util.reFind(input('[   ðº   ]:è¾å¥æé³ç´æ­é´webç«¯é¾æ¥ï¼ä¾å¦ https://live.douyin.com/176819813905ï¼'))[0]

if live_url == '':
    Util.reFind(input('[   ðº   ]:è¯·è¾å¥æ­£ç¡®çé¾æ¥ï¼'))[0]

json = Util.Lives.get_Live(live_url)

# æ¯å¦å¨æ­
status = json['data']['data'][0]['status']

if status == 4:
    input('[   ðº   ]:å½åç´æ­å·²ç»æï¼æåè½¦éåº')
    exit(0)

# ç´æ­æ é¢
title = json['data']['data'][0]['title']

# è§çäººæ°
user_count = json['data']['data'][0]['user_count_str']

# æµç§°
nickname = json['data']['data'][0]['owner']['nickname']

# sec_uid
sec_uid = json['data']['data'][0]['owner']['sec_uid']

# ç´æ­é´è§çç¶æ
display_long = json['data']['data'][0]['room_view_stats']['display_long']

# æ¨æµ
flv_pull_url = json['data']['data'][0]['stream_url']['flv_pull_url']

try:
    # ååº
    partition = json['data']['partition_road_map']['partition']['title']
    sub_partition = json['data']['partition_road_map']['sub_partition']['partition']['title']
except Exception as e:
    partition = 'æ '
    sub_partition = 'æ '

info = '[   ð»   ]:ç´æ­é´ï¼%s  å½å%s  ä¸»æ­ï¼%s  ååºï¼%s-%s\r' % (
    title, display_long, nickname, partition, sub_partition)
print(info)

flv = []
print('[   ð¦   ]:ç´æ­é´æ¸æ°åº¦')
for i, f in enumerate(flv_pull_url.keys()):
    print('[   %s   ]: %s' % (i, f))
    flv.append(f)

rate = int(input('[   ð¬   ]è¾å¥æ°å­éæ©æ¨æµæ¸æ°åº¦ï¼'))

# ld = æ æ¸

# sd = é«æ¸

# hd = è¶æ¸

# uhd = èå

# or4 = åç»

# æ¾ç¤ºæ¸æ°åº¦åè¡¨
print('[   %s   ]:%s' % (flv[rate], flv_pull_url[flv[rate]]))

input('[   ðº   ]:å¤å¶é¾æ¥ä½¿ç¨ä¸è½½å·¥å·ä¸è½½ï¼æåè½¦éåº')