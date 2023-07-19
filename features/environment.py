from selenium import webdriver
import allure
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option('detach', True)
options.add_argument("--headless=new")


def before_scenario(context, driver):
    context.driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    context.driver.implicitly_wait(30)


def after_step(context, step):
    print()

    allure.attach(context.driver.get_screenshot_as_png(), name='screenshot',
                  attachment_type=allure.attachment_type.PNG)
