# example.py
import TikTokDownload as TK
import Util

# 单视频下载
# TK.video_download(*TK.main())

# 批量下载
if __name__ == '__main__':
    # 获取命令行参数
    cmd = Util.Command()
    # 获取用户主页数据
    profile = Util.Profile()
    # 使用参数，没有则使用默认参数并下载
    profile.getProfile(cmd.setting())
	# 如果需要定时下载则注释这个input
    input('[  完成  ]:已完成批量下载，输入任意键后退出:')

    """git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/tianhai121/douyin_download.git
git push -u origin main"""