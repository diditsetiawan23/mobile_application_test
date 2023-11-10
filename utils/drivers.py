import os
from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.configuration import config

appium_server_url = 'http://localhost:4723'
apk_path = os.getcwd()+os.path.join('/test_assets','apk','login_sample.apk') 

def get_des_cap():
    des_cap = {
        'app': f'{apk_path}', # (Path of the app to automate)
        'automationName' : 'UiAutomator2',
        'platformName' : 'android',
        'udid' : f'{config.get("udid")}', 
        'appPackage':'com.loginmodule.learning',
        'appActivity':'com.loginmodule.learning.activities.LoginActivity',
        'noReset' : 'true',
        'appWaitForLaunch' : 'false',
        'newCommandTimeout' : '120',
        'autoAcceptAlerts' : 'true',
        'shouldTerminateApp': 'true'
        }
    return des_cap

# Converts capabilities to AppiumOptions instance
capabilities_options = UiAutomator2Options().load_capabilities(get_des_cap())
#driver initialization
driver = webdriver.Remote(command_executor=appium_server_url, options=capabilities_options)