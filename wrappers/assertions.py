from wrappers import interaction as WebUI
from selenium.common.exceptions import NoSuchElementException, TimeoutException

## Assert Element is Present
def element_is_present(by, test, object):
    try:
        element = WebUI.find_element(by, object)
        # Assert that the element is present
        if element is not None:
            WebUI.log_report(f"Element '{object}' accessed by '{by}' is present",test, 'pass')
        else:
            WebUI.log_report(f"Element '{object}' accessed by '{by}' is not present",test, 'fail')
    except NoSuchElementException:
        WebUI.log_report(f"NoSuchElementException - Element {object} is not found", test, 'fail')
    except TimeoutException:
        WebUI.log_report(f"TimeoutException - Element {object} is not found", test, 'fail')

## Assert Element is Clickable
def element_is_clickable(by, test, object):
    try:
        element = WebUI.find_element(by, object)
        # Assert that the element is enabled
        if element.is_enabled():
            WebUI.log_report(f"Element '{object}' accessed by '{by}' is clickable",test, 'pass')
        else:
            WebUI.log_report(f"Element '{object}' accessed by '{by}' is not clickable",test, 'fail')
    except NoSuchElementException:
        WebUI.log_report(f"NoSuchElementException - Element {object} is not found", test, 'fail')
    except TimeoutException:
        WebUI.log_report(f"TimeoutException - Element {object} is not found", test, 'fail')    

## Assert Text from Textinput
def text_from_textinput(by, test, object, text):
    try:
        actual_text = WebUI.get_text_from_textinput(by,test, object)
        # Assert actual text is same with expected
        if actual_text == text:
            WebUI.log_report(f"Actual text on textinput {object} is '{actual_text}', while expected text is {text}",test, 'pass')
        else:
            WebUI.log_report(f"Actual text on textinput {object} is '{actual_text}', while expected text is {text}",test, 'fail')
    except NoSuchElementException:
        WebUI.log_report(f"NoSuchElementException - Element {object} is not found", test, 'fail')
    except TimeoutException:
        WebUI.log_report(f"TimeoutException - Element {object} is not found", test, 'fail')

## Assert Text from Element
def text_from_element(by, test,object, text):
    try:
        actual_text = WebUI.get_text_from_element(by,test, object)
        # Assert actual text is same with expected
        if actual_text == text:
            WebUI.log_report(f"Actual text on element {object} is '{actual_text}', while expected text is {text}",test, 'pass')
        else:
            WebUI.log_report(f"Actual text on element {object} is '{actual_text}', while expected text is {text}",test, 'fail')
    except NoSuchElementException:
        WebUI.log_report(f"NoSuchElementException - Element {object} is not found", test, 'fail')
    except TimeoutException:
        WebUI.log_report(f"TimeoutException - Element {object} is not found", test, 'fail')


## Populate Assert Element is Present
def element_is_present_by_classname(test,object):
    element_is_present('classname',test, object)
def element_is_present_by_cssselector(test,object):
    element_is_present('cssselector',test, object)
def element_is_present_by_id(test, object):
    element_is_present('id',test, object)
def element_is_present_by_name(test, object):
    element_is_present('name',test, object)
def element_is_present_by_linktext(test, object):
    element_is_present('linktext',test, object)
def element_is_present_by_partiallinktext(test, object):
    element_is_present('partiallinktext',test, object)
def element_is_present_by_tagname(test, object):
    element_is_present('tagname', test,object)
def element_is_present_by_xpath(test, object):
    element_is_present('xpath', test,object)
## Populate Assert Element is Clickable
def element_is_clickable_by_classname(test, object):
    element_is_clickable('classname', test,object)
def element_is_clickable_by_cssselector(test, object):
    element_is_clickable('cssselector', test,object)
def element_is_clickable_by_id(test, object):
    element_is_clickable('id', test,object)
def element_is_clickable_by_name(test, object):
    element_is_clickable('name', test,object)
def element_is_clickable_by_linktext(test, object):
    element_is_clickable('linktext', test,object)
def element_is_clickable_by_partiallinktext(test, object):
    element_is_clickable('partiallinktext', test,object)
def element_is_clickable_by_tagname(test, object):
    element_is_clickable('tagname', test,object)
def element_is_clickable_by_xpath(test, object):
    element_is_clickable('xpath', test,object)
## Populate Assert Text from Textinput
def text_from_textinput_by_classname(test, object, text):
    text_from_textinput('classname', test, object, text)
def text_from_textinput_by_cssselector(test, object, text):
    text_from_textinput('cssselector', test, object, text)
def text_from_textinput_by_id(test, object, text):
    text_from_textinput('id', test, object, text)
def text_from_textinput_by_name(test, object, text):
    text_from_textinput('name', test, object, text)
def text_from_textinput_by_linktext(test, object, text):
    text_from_textinput('linktext', test, object, text)
def text_from_textinput_by_partiallinktext(test, object, text):
    text_from_textinput('partiallinktext', test, object, text)
def text_from_textinput_by_tagname(test, object, text):
    text_from_textinput('tagname', test, object, text)
def text_from_textinput_by_xpath(test, object, text):
    text_from_textinput('xpath', test, object, text)
## Populate Assert Text from Element
def text_from_element_by_classname(test, object, text):
    text_from_element('classname', test, object, text)
def text_from_element_by_cssselector(test, object, text):
    text_from_element('cssselector', test, object, text)
def text_from_element_by_id(test, object, text):
    text_from_element('id', test, object, text)
def text_from_element_by_name(test, object, text):
    text_from_element('name', test, object, text)
def text_from_element_by_linktext(test, object, text):
    text_from_element('linktext', test, object, text)
def text_from_element_by_partiallinktext(test, object, text):
    text_from_element('partiallinktext', test, object, text)
def text_from_element_by_tagname(test, object, text):
    text_from_element('tagname',test, object, text)
def text_from_element_by_xpath(test, object, text):
    text_from_element('xpath', test, object, text)
