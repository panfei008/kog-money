
import os
import logging

from constant import PC_PROJECT_ROOT,PC_CROP_PARENT_NAME,PC_CROP_PARENT_PATH,SCREEN_FILE_NAME,SCREEN_FILE_TYPE,SCREEN_PATH
# 日志输出
from logger import logger as logging


#解决小米手机miui12生成截图文件后面可能会带时间戳，如指定screen.png实际为screen_1603558927241.png
def screen_crop_fix():
    if not os.path.exists(PC_CROP_PARENT_PATH):
        os.makedirs(PC_CROP_PARENT_PATH)

    count = 0
    while True:
        name="{}/{}{}{}".format(PC_CROP_PARENT_PATH,SCREEN_FILE_NAME,count,SCREEN_FILE_TYPE)
        if os.path.exists(name):
            count = count+1
            continue
        os.system('adb shell rm -r /sdcard/{}'.format(PC_CROP_PARENT_NAME))
        os.system('adb shell mkdir /sdcard/{}'.format(PC_CROP_PARENT_NAME))

        os.system('adb shell screencap -p /sdcard/{}/{}'.format(PC_CROP_PARENT_NAME,SCREEN_PATH))
        os.system('adb pull /sdcard/{} {}'.format(PC_CROP_PARENT_NAME,PC_PROJECT_ROOT))

        logging.debug("截图成功")
        break

def screen_crop():
    if not os.path.exists(PC_CROP_PARENT_PATH):
        os.makedirs(PC_CROP_PARENT_PATH)
    count = 0
    error_count = 0
    while True:
        name="{}/{}{}{}".format(PC_CROP_PARENT_PATH,SCREEN_FILE_NAME,count,SCREEN_FILE_TYPE)
        if os.path.exists(name):
            count = count + 1
            continue


        os.system('adb shell screencap -p /sdcard/{}'.format(SCREEN_PATH))
        os.system('adb pull /sdcard/{} {}'.format(SCREEN_PATH,name))
        if os.path.exists(name):
            logging.debug("截图成功:{}".format(name))
            break
        else:
            logging.debug("截图失败")
            error_count = error_count + 1
            if error_count>=3:
                break
if __name__ == '__main__':
    screen_crop()



