from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given(u'I am on the QA01 test site')
def step_impl(context):
    context.driver.get("https://QA01.livedata.com/")
    context.driver.maximize_window()


@When(u'I click the link for the PerOpPlanner')
def step_impl(context):
    context.driver.implicitly_wait(10)
    context.driver.find_element(by=By.LINK_TEXT, value="PeriOpPlanner").click()


@Then(u'I enter the userid and password')
def step_impl(context):
    context.driver.implicitly_wait(10)
    context.driver.find_element(by=By.ID, value="loginScreenUsername").send_keys("superuser")
    context.driver.find_element(by=By.ID, value="loginScreenPassword").send_keys("livedata")


@Then(u'I click the login button')
def step_impl(context):
    context.driver.find_element(by=By.ID, value="loginButton").click()


@Then(u'I am on the periOpPlanner page')
def step_impl(context):
    print(u'STEP: Then I am on the periOpPlanner page')


@Then(u'I click the menudropdown button')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.driver.find_element(by=By.ID, value="menuDropdownTrigger").click()


@then(u'I select the block option')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.driver.find_element(by=By.ID, value="menuServiceBlockPlanner").click()


@then(u'I click the create button')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.driver.find_element(by=By.ID, value="weeklyCreateButton").click()


@then(u'I select the Start Time as "{starttime}"')
def step_impl(context, starttime):
    input_field = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='serviceStartTime']/div/auto-complete/input"))
    )
    input_field.clear()
    input_field.send_keys(starttime)
    input_field.send_keys(Keys.ENTER)


@then(u'I select the End Time as "{endtime}"')
def step_impl(context, endtime):
    input_field = WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='serviceEndTime']/div/auto-complete/input"))
    )
    input_field.clear()
    input_field.send_keys(endtime)
    input_field.send_keys(Keys.ENTER)


@then(u'I select the Room as "{room}"')
def step_impl(context, room):
    context.driver.implicitly_wait(20)
    dropdown = context.driver.find_element(by=By.XPATH,
                                           value="//*[@id='serviceBlockRoomSelector']/div/div[2]/select")
    select = Select(dropdown)
    select.select_by_visible_text(room)


@then(u'I select the Block Group as "{blockgroup}"')
def step_impl(context, blockgroup):
    dropdown = context.driver.find_element(by=By.XPATH,
                                           value="//*[@id='serviceBlockBlockGroupSelector']/div/div[2]/select")
    select = Select(dropdown)
    select.select_by_visible_text(blockgroup)


@then(u'I click on the save button')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.driver.find_element(by=By.ID, value="saveButton").click()


@then(u'I am on the ReasonSelector screen')
def step_impl(context):
    print(u'I am on the ReasonSelector screen')


@then(u'I select any reason')
def step_impl(context):
    dropdown = context.driver.find_element(by=By.ID,
                                           value="confirmDropdownTrigger")
    select = Select(dropdown)
    select.select_by_value("1160")


@then(u'I click on the confirm button')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.driver.find_element(by=By.ID, value="confirmOverrideButton").click()
