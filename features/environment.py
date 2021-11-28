import os
import platform

from selenium.webdriver import Chrome


def before_feature(context, feature):
    if platform.system() == "Windows":
        path = 'drivers\\chromedriver.exe'
    elif platform.system() == "Linux":
        path = 'drivers\\chromedriver_linux'
    elif platform.system() == "Darwin":
        path = 'drivers\\chromedriver_mac'

    context.driver = Chrome(executable_path=path)

def after_feature(context, feature):
    context.driver.close()

# run after each test
# def before_all(context):
# def after_all(context):
