import time
from wrappers import wrap
from utils.drivers import driver
from utils import htmlreport as report
# from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# initiate logger
logger = wrap.logger

# initiate log for reporting
logstatus = report.LogStatus

## returning by statement
def get_by(by):
    if by=='classname':
        by_return = By.CLASS_NAME
    elif by=='cssselector':
        by_return = By.CSS_SELECTOR
    elif by=='id':
        by_return = By.ID
    elif by=='name':
        by_return = By.NAME 
    elif by=='linktext':
        by_return = By.LINK_TEXT  
    elif by=='partiallinktext':
        by_return = By.PARTIAL_LINK_TEXT
    elif by=='tagname':
        by_return = By.TAG_NAME
    elif by=='xpath':
        by_return = By.XPATH
    return by_return

# log and report log
def log_report(txt,test,status):
    wrap.print_log_file(txt)
    if status == 'pass':
        status_log = logstatus.PASS
    elif status == 'fail':
        status_log = logstatus.FAIL
    elif status == 'warning':
        status_log = logstatus.WARNING
    elif status == 'info':
        status_log = logstatus.INFO
    test.log(status_log,txt)

## Find Element
def find_element(by, object):
    locators = get_by(by)
    return WebDriverWait(driver, timeout=10).until(
        EC.presence_of_element_located((locators, object))
    )

## Click Action
def click_element(by, test, object):
    txt = f"Clicking by '{by}' on element '{object}'"
    log_report(txt, test,'info')
    try:
        element = find_element(by, object)
        element.click()
    except Exception as e:
        log_report(e, test, 'fail')

## Clear Text Action
def clear_text_element(by, test, object):
    txt = f"Clearing text by '{by}' on element '{object}'"
    log_report(txt, test,'info')
    try:
        element = find_element(by, object)
        element.clear()
    except Exception as e:
        log_report(e, test, 'fail')

## Send Text Action
def sendtext_element(by, test, object, text):
    txt = f"Send text '{text}' by '{by}' on element '{object}'"
    log_report(txt, test, 'info')
    try:
        element = find_element(by, object)
        element.send_keys(text)
    except Exception as e:
        log_report(e, test, 'fail')

## Explicit wait clickable
def wait_element_clickable(by, test, object,timeout):
    txt = f"Wait element '{object}' clickable by '{by}'"
    log_report(txt, test, 'info')
    try:
        locators = get_by(by)
        wait = WebDriverWait(driver, timeout=timeout)
        wait.until(EC.element_to_be_clickable((locators, object)))
    except Exception as e:
        log_report(e, test, 'fail')

## Explicit wait displayed   
def wait_element_displayed(by,test, object,timeout):
    txt = f"Wait element '{object}' displayed by '{by}'"
    log_report(txt, test, 'info')
    try:
        locators = get_by(by)
        wait = WebDriverWait(driver, timeout=timeout)
        wait.until(EC.visibility_of_element_located((locators, object)))
    except Exception as e:
        log_report(e, test, 'fail')

## Get text from Text Input
def get_text_from_textinput(by, test, object):
    txt = f"Get text from textinput by '{by}' on element '{object}'"
    log_report(txt, test, 'info')
    try:
        element = find_element(by, object)
        text = element.get_attribute('value')
        return text
    except Exception as e:
        log_report(e, test, 'fail')

## Get text from element
def get_text_from_element(by, test, object):
    txt = f"Get text from element by '{by}' on element '{object}'"
    log_report(txt, test, 'info')
    try:
        element = find_element(by, object)
        text = element.text
        return text
    except Exception as e:
        log_report(e, test, 'fail')

## Select from dropdown
def select_dropdown(by, test, object, by_selector, value):
    txt = f"Selecting option from element by '{by}' on element '{object}'"
    log_report(txt, test, 'info')
    try:
        element = find_element(by, object)
        selector = Select(element)
        if by_selector == 'index':
            selector.select_by_index(value)
        elif by_selector == 'value':
            selector.select_by_value(value)
        elif by_selector == 'visible_text':
            selector.select_by_visible_text(value)
    except Exception as e:
        log_report(e, test, 'fail')

## Sleep function
def sleep(seconds:int):
    logger.info(f"Waiting for {seconds} seconds")
    time.sleep(seconds)

## Reset
def relaunch():
    driver.terminate_app('com.loginmodule.learning')
    driver.activate_app('com.loginmodule.learning')

## Populate Find Elements
def find_element_by_classname(test,object):
    find_element('classname', object)
def find_element_by_cssselector(test,object):
    find_element('cssselector', object)
def find_element_by_id(test,object):
    find_element('id', object)
def find_element_by_name(test,object):
    find_element('name', object)
def find_element_by_linktext(test,object):
    find_element('linktext', object)
def find_element_by_partiallinktext(test,object):
    find_element('partiallinktext', object)
def find_element_by_tagname(test,object):
    find_element('tagname', object)
def find_element_by_xpath(test,object):
    find_element('xpath', object)
## Populate Click Action
def click_element_by_classname(test,object):
    click_element('classname', test,object)
def click_element_by_cssselector(test,object):
    click_element('cssselector', test,object)
def click_element_by_id(test,object):
    click_element('id', test,object)
def click_element_by_name(test,object):
    click_element('name', test,object)
def click_element_by_linktext(test,object):
    click_element('linktext', test,object)
def click_element_by_partiallinktext(test,object):
    click_element('partiallinktext', test,object)
def click_element_by_tagname(test,object):
    click_element('tagname', test,object)
def click_element_by_xpath(test,object):
    click_element('xpath', test, object)
## Populate Clear Action
def clear_element_by_classname(test,object):
    clear_text_element('classname', test, object)
def clear_element_by_cssselector(test,object):
    clear_text_element('cssselector', test, object)
def clear_element_by_id(test,object):
    clear_text_element('id', test, object)
def clear_element_by_name(test,object):
    clear_text_element('name', test, object)
def clear_element_by_linktext(test,object):
    clear_text_element('linktext', test, object)
def clear_element_by_partiallinktext(test,object):
    clear_text_element('partiallinktext', test, object)
def clear_element_by_tagname(test,object):
    clear_text_element('tagname', test, object)
def clear_element_by_xpath(test,object):
    clear_text_element('xpath', test, object)
## Populate Send Text Action
def sendtext_element_by_classname(test, object, text):
    sendtext_element('classname', test, object, text)
def sendtext_element_by_cssselector(test, object, text):
    sendtext_element('cssselector', test, object, text)
def sendtext_element_by_id(test, object, text):
    sendtext_element('id', test, object, text)
def sendtext_element_by_name(test, object, text):
    sendtext_element('name', test, object, text)
def sendtext_element_by_linktext(test, object, text):
    sendtext_element('linktext', test, object, text)
def sendtext_element_by_partiallinktext(test, object, text):
    sendtext_element('partiallinktext', test, object, text)
def sendtext_element_by_tagname(test, object, text):
    sendtext_element('tagname', test, object, text)
def sendtext_element_by_xpath(test, object, text):
    sendtext_element('xpath', test, object, text)         
## Populate Explicit Wait
def wait_element_clickable_by_classname(test,object,timeout):
    wait_element_clickable('classname',test,object,timeout)
def wait_element_clickable_by_cssselector(test,object,timeout):
    wait_element_clickable('cssselector',test,object,timeout)
def wait_element_clickable_by_id(test,object,timeout):
    wait_element_clickable('id',test,object,timeout)
def wait_element_clickable_by_name(test,object,timeout):
    wait_element_clickable('name',test,object,timeout)
def wait_element_clickable_by_linktext(test,object,timeout):
    wait_element_clickable('linktext',test,object,timeout)
def wait_element_clickable_by_partiallinktext(test,object,timeout):
    wait_element_clickable('partiallinktext',test,object,timeout)
def wait_element_clickable_by_tagname(test,object,timeout):
    wait_element_clickable('tagname',test,object,timeout)
def wait_element_clickable_by_xpath(test,object,timeout):
    wait_element_clickable('xpath',test,object,timeout)
def wait_element_displayed_by_classname(test,object,timeout):
    wait_element_displayed('classname',test,object,timeout)
def wait_element_displayed_by_cssselector(test,object,timeout):
    wait_element_displayed('cssselector',test,object,timeout)
def wait_element_displayed_by_id(test,object,timeout):
    wait_element_displayed('id',test,object,timeout)
def wait_element_displayed_by_name(test,object,timeout):
    wait_element_displayed('name',test,object,timeout)
def wait_element_displayed_by_linktext(test,object,timeout):
    wait_element_displayed('linktext',test,object,timeout)
def wait_element_displayed_by_partiallinktext(test,object,timeout):
    wait_element_displayed('partiallinktext',test,object,timeout)
def wait_element_displayed_by_tagname(test,object,timeout):
    wait_element_displayed('tagname',test,object,timeout)
def wait_element_displayed_by_xpath(test,object,timeout):
    wait_element_displayed('xpath',test,object,timeout)
    ## Populate Get Text from Text Input
def get_text_from_textinput_by_classname(test,object):
    get_text_from_textinput('classname',test, object)
def get_text_from_textinput_by_cssselector(test,object):
    get_text_from_textinput('cssselector',test, object)
def get_text_from_textinput_by_id(test,object):
    get_text_from_textinput('id',test,object)
def get_text_from_textinput_by_name(test,object):
    get_text_from_textinput('name',test,object)
def get_text_from_textinput_by_linktext(test,object):
    get_text_from_textinput('linktext',test,object)
def get_text_from_textinput_by_partiallinktext(test,object):
    get_text_from_textinput('partiallinktext',test,object)
def get_text_from_textinput_by_tagname(test,object):
    get_text_from_textinput('tagname',test,object)
def get_text_from_textinput_by_xpath(test,object):
    get_text_from_textinput('xpath',test,object)
## Populate Get Text from Element
def get_text_from_element_by_classname(test,object):
    get_text_from_element('classname',test,object)
def get_text_from_element_by_cssselector(test,object):
    get_text_from_element('cssselector',test,object)
def get_text_from_element_by_id(test,object):
    get_text_from_element('id',test,object)
def get_text_from_element_by_name(test,object):
    get_text_from_element('name',test,object)
def get_text_from_element_by_linktext(test,object):
    get_text_from_element('linktext',test,object)
def get_text_from_element_by_partiallinktext(test,object):
    get_text_from_element('partiallinktext',test,object)
def get_text_from_element_by_tagname(test,object):
    get_text_from_element('tagname',test,object)
def get_text_from_element_by_xpath(test,object):
    get_text_from_element('xpath',test,object)
## Populates Select from Dropdown
def select_dropdown_index_by_xpath(test, object, value):
    select_dropdown('xpath',test, object,'index',value)
def select_dropdown_value_by_xpath(test, object, value):
    select_dropdown('xpath',test, object,'value',value)
def select_dropdown_visibletext_by_xpath(test, object, value):
    select_dropdown('xpath',test, object,'value',value)
def select_dropdown_index_by_id(test, object, value):
    select_dropdown('id',test, object,'index',value)
def select_dropdown_value_by_id(test, object, value):
    select_dropdown('id',test, object,'value',value)
def select_dropdown_visibletext_by_id(test, object, value):
    select_dropdown('id',test, object,'value',value)
def select_dropdown_index_by_name(test, object, value):
    select_dropdown('name',test, object,'index',value)
def select_dropdown_value_by_name(test, object, value):
    select_dropdown('name',test, object,'value',value)
def select_dropdown_visibletext_by_name(test, object, value):
    select_dropdown('name',test, object,'value',value)
def select_dropdown_index_by_classname(test, object, value):
    select_dropdown('classname',test, object,'index',value)
def select_dropdown_value_by_classname(test, object, value):
    select_dropdown('classname',test, object,'value',value)
def select_dropdown_visibletext_by_classname(test, object, value):
    select_dropdown('classname',test, object,'value',value)
def select_dropdown_index_by_cssselector(test, object, value):
    select_dropdown('cssselector',test,object,'index',value)
def select_dropdown_value_by_cssselector(test, object, value):
    select_dropdown('cssselector',test,object,'value',value)
def select_dropdown_visibletext_by_cssselector(test, object, value):
    select_dropdown('cssselector',test,object,'value',value)
def select_dropdown_index_by_linktext(test, object, value):
    select_dropdown('linktext',test,object,'index',value)
def select_dropdown_value_by_linktext(test, object, value):
    select_dropdown('linktext',test,object,'value',value)
def select_dropdown_visibletext_by_linktext(test, object, value):
    select_dropdown('linktext',test,object,'value',value)
def select_dropdown_index_by_partiallinktext(test, object, value):
    select_dropdown('partiallinktext',test,object,'index',value)
def select_dropdown_value_by_partiallinktext(test, object, value):
    select_dropdown('partiallinktext',test,object,'value',value)
def select_dropdown_visibletext_by_partiallinktext(test, object, value):
    select_dropdown('partiallinktext',test,object,'value',value)
def select_dropdown_index_by_tagname(test, object, value):
    select_dropdown('tagname',test,object,'index',value)
def select_dropdown_value_by_tagname(test, object, value):
    select_dropdown('tagname',test,object,'value',value)
def select_dropdown_visibletext_by_tagname(test, object, value):
    select_dropdown('tagname',test,object,'value',value)