import unittest
from wrappers import interaction as WebUI
from wrappers import assertions as asserting
from wrappers import wrap as functions
from object_repository.web_elements import login_screen
from object_repository.variables import login as data

# Preparation
extent, parent, log_status, sub_parent = functions.init_extent_report('Login')

# Test Template
def login_base_test(test,json_data:dict):
    data =  json_data
    # Wait element accessible
    WebUI.relaunch()
    WebUI.wait_element_clickable_by_id(test,login_screen.input_email_id, 30)
    # Fill Email Field
    if data["email"] != "":
        WebUI.sendtext_element_by_id(test,login_screen.input_email_id, data["email"])
    # Fill password Field
    if data["password"] != "":
        WebUI.sendtext_element_by_id(test,login_screen.input_password_id, data["password"])
    # Click Login button
    WebUI.click_element_by_id(test,login_screen.btn_login_id)
    # return alertText
    return data["assertText"]
   

class LoginTestCase(unittest.TestCase):
    def test_001_login_without_email_and_password(self):
        # start testcase
        test = functions.init_test_cases(sub_parent, 'Login Without Email & Password')
        # execute test
        alert_test = login_base_test(test,data.login_without_email_and_password)
        # check alert appear
        asserting.element_is_clickable_by_xpath(test,login_screen.error_input_email_xpath)
        # check alert text
        asserting.text_from_element_by_xpath(test,login_screen.error_input_email_xpath, alert_test)

    def test_002_login_without_password(self):
        # start testcase
        test = functions.init_test_cases(sub_parent, 'Login Without Password')
        # execute test
        alert_test = login_base_test(test,data.login_without_password)
        # check alert appear
        asserting.element_is_clickable_by_xpath(test, login_screen.error_input_password_xpath)
        # check alert text
        asserting.text_from_element_by_xpath(test, login_screen.error_input_password_xpath, alert_test)

    def test_003_login_without_email(self):
        # start testcase
        test = functions.init_test_cases(sub_parent, 'Login Without Email')
        # execute test
        alert_test = login_base_test(test,data.login_without_email)
        # check alert appear
        asserting.element_is_clickable_by_xpath(test, login_screen.error_input_email_xpath)
        # check alert text
        asserting.text_from_element_by_xpath(test, login_screen.error_input_email_xpath, alert_test)
    
    def test_004_login_with_notvalid_email(self):
        # start testcase
        test = functions.init_test_cases(sub_parent, 'Login With Not Valid Email')
        # execute test
        alert_test = login_base_test(test,data.login_with_notvalid_email)
        # check alert appear
        asserting.element_is_clickable_by_xpath(test, login_screen.error_input_email_xpath)
        # check alert text
        asserting.text_from_element_by_xpath(test, login_screen.error_input_email_xpath, alert_test)

    def test_005_login_with_unregistered_email(self):
        # start testcase
        test = functions.init_test_cases(sub_parent, 'Login With Unregistered Email')
        # execute test
        alert_test = login_base_test(test,data.login_with_unregistered_email)
        # check alert appear
        asserting.element_is_clickable_by_xpath(test, login_screen.error_input_email_xpath)
        # check alert text
        asserting.text_from_element_by_xpath(test, login_screen.error_input_email_xpath, alert_test)

    def test_006_login_with_nomatch_email_password(self):
        # start testcase
        test = functions.init_test_cases(sub_parent, 'Login With Not Match Email & Password')
        # execute test
        alert_test = login_base_test(test,data.login_with_nomatch_email_password)
        # check alert appear
        asserting.element_is_clickable_by_id(test, login_screen.error_failed_login_id)
        # check alert text
        asserting.text_from_element_by_id(test, login_screen.error_failed_login_id, alert_test)
    
    def test_007_login_with_valid_email_password(self):
        # start testcase
        test = functions.init_test_cases(sub_parent, 'Login With Valid Email & Password')
        # execute test
        alert_test = login_base_test(test,data.login_with_valid_email_password)
        # check alert appear
        asserting.element_is_clickable_by_xpath(test, login_screen.success_login_name)
        # check alert appear
        asserting.element_is_clickable_by_xpath(test, login_screen.success_login_name)

    def test_008_click_on_register_button(self):
        # start testcase 
        test = functions.init_test_cases(sub_parent, 'Click on Register Button')
        # Click on register button
        WebUI.click_element_by_id(test, login_screen.btn_to_register_id)
        # Check register screen appear by identify submit button
        asserting.element_is_clickable_by_id(test, login_screen.btn_register_id)


    def test_999_ShutDownTest(self):
        # calling wrapper to end the test
        functions.extent_end_test(extent)


if __name__ == "__main__":
    unittest.main()



