from selenium.webdriver import Chrome

def before_feature(context, feature):
    path = 'drivers\\chromedriver.exe'
    context.driver = Chrome(executable_path=path)

def after_feature(context, feature):
    context.driver.close()

# run after each test
# def before_all(context):
# def after_all(context):