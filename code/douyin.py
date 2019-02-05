# -*- encoding=utf8 -*-
__author__ = "meteorix"

from airtest.core.api import *

# 为了py运行，先不自动设置了
# auto_setup(__file__)

# 设置log目录，用于保存截图
set_logdir(".")

# 安卓模拟器的必备参数
init_device("Android", cap_method="javacap")


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


APP = "com.ss.android.ugc.aweme"

stop_app(APP)
start_app(APP)


# 点右下角的“我”
# poco(text="我").click()
# 点“x”退回来
# poco("com.ss.android.ugc.aweme:id/a54").click()

# 等待加载好界面
poco(text="我").wait()
poco("com.ss.android.ugc.aweme:id/al8").wait()

sleep(1.0)


for i in range(10):
    # 划一条
    poco("com.ss.android.ugc.aweme:id/ak2").swipe([0, -0.6])
    sleep(1.0)
    # 点个赞
    poco("com.ss.android.ugc.aweme:id/al8").click()
    if poco(text="输入手机号码").exists():
        # TODO: 自动登录
        print("先手动登录一下吧~")
        break
    # 截个图
    snapshot()
