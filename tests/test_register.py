import unittest
from wrappers import interaction as WebUI
from wrappers import assertions as asserting
from wrappers import wrap as functions
from object_repository.web_elements import register_screen
from object_repository.variables import register as data

# Preparation
extent, parent, log_status, sub_parent = functions.init_extent_report('Register')

# Test Template
def register_base_test(test, json_data:dict):
    data = json_data
    # Wait element accessible
    WebUI.relaunch()
    WebUI.wait_element_clickable_by_id(test, register_screen.btn_to_register_id,30)
    # Click on button Register
    WebUI.click_element_by_id(test, register_screen.btn_to_register_id)
    # Fill Name
    if data["name"] != "":
        WebUI.sendtext_element_by_id(test, register_screen.input_name_id, data["name"])
    # Fill Email
    if data["email"] != "":
        WebUI.sendtext_element_by_id(test, register_screen.input_email_id, data["email"])
    # Fill Password
    if data["password"] != "":
        WebUI.sendtext_element_by_id(test, register_screen.input_password_id, data["password"])
    # Fill Confirm Password 
    if data["pass_confirm"] != "":
        WebUI.sendtext_element_by_id(test, register_screen.input_confirm_password_id, data["pass_confirm"])
    # Click Register button
    WebUI.click_element_by_id(test, register_screen.btn_register_id)
    # return alertText
    return data["assertText"]

class RegisterTestCase(unittest.TestCase):
    def test_001_register_without_fill_all_data(self):
        # start testcase
        test = functions.init_test_cases(sub_parent, 'Register Without Fill All Data')
        # execute test
        alert_test = register_base_test(test,data.register_without_fill_all_data)
        # check alert appear
        asserting.element_is_clickable_by_xpath(test,register_screen.error_input_name_xpath)
        # check alert text
        asserting.text_from_element_by_xpath(test,register_screen.error_input_name_xpath, alert_test)

    def test_002_register_only_fill_name(self):
        # start testcase
        test = functions.init_test_cases(sub_parent, 'Register With Only Fill Name')
        # execute test
        alert_test = register_base_test(test,data.register_only_fill_name)
        # check alert appear
        asserting.element_is_clickable_by_xpath(test,register_screen.error_input_email_xpath)
        # check alert text
        asserting.text_from_element_by_xpath(test,register_screen.error_input_email_xpath, alert_test)

    def test_003_register_only_fill_email(self):
        # start testcase
        test = functions.init_test_cases(sub_parent, 'Register With Only Fill Email')
        # execute test
        alert_test = register_base_test(test,data.register_only_fill_email)
        # check alert appear
        asserting.element_is_clickable_by_xpath(test,register_screen.error_input_name_xpath)
        # check alert text
        asserting.text_from_element_by_xpath(test,register_screen.error_input_name_xpath, alert_test)

    def test_004_register_only_fill_password(self):
        # start testcase
        test = functions.init_test_cases(sub_parent, 'Register With Only Fill Password')
        # execute test
        alert_test = register_base_test(test,data.register_only_fill_password)
        # check alert appear
        asserting.element_is_clickable_by_xpath(test,register_screen.error_input_name_xpath)
        # check alert text
        asserting.text_from_element_by_xpath(test,register_screen.error_input_name_xpath, alert_test)

    def test_005_register_only_fill_confirmpassword(self):
        # start testcase
        test = functions.init_test_cases(sub_parent, 'Register With Only Fill Confirm Password')
        # execute test
        alert_test = register_base_test(test,data.register_only_fill_confirmpassword)
        # check alert appear
        asserting.element_is_clickable_by_xpath(test,register_screen.error_input_name_xpath)
        # check alert text
        asserting.text_from_element_by_xpath(test,register_screen.error_input_name_xpath, alert_test)

    def test_006_register_fill_all_except_name(self):
        # start testcase
        test = functions.init_test_cases(sub_parent, 'Register Fill All Except Name')
        # execute test
        alert_test = register_base_test(test,data.register_fill_all_except_name)
        # check alert appear
        asserting.element_is_clickable_by_xpath(test,register_screen.error_input_name_xpath)
        # check alert text
        asserting.text_from_element_by_xpath(test,register_screen.error_input_name_xpath, alert_test)
    
    def test_007_register_only_fill_all_except_email(self):
        # start testcase
        test = functions.init_test_cases(sub_parent, 'Register Fill All Except Email')
        # execute test
        alert_test = register_base_test(test,data.register_only_fill_all_except_email)
        # check alert appear
        asserting.element_is_clickable_by_xpath(test,register_screen.error_input_email_xpath)
        # check alert text
        asserting.text_from_element_by_xpath(test,register_screen.error_input_email_xpath, alert_test)

    def test_008_register_only_fill_all_except_password(self):
        # start testcase
        test = functions.init_test_cases(sub_parent, 'Register Fill All Except Password')
        # execute test
        alert_test = register_base_test(test,data.register_only_fill_all_except_password)
        # check alert appear
        asserting.element_is_clickable_by_xpath(test,register_screen.error_input_password_xpath)
        # check alert text
        asserting.text_from_element_by_xpath(test,register_screen.error_input_password_xpath, alert_test)

    def test_009_register_only_fill_all_except_confirmpassword(self):
        # start testcase
        test = functions.init_test_cases(sub_parent, 'Register Fill All Except Confirm Password')
        # execute test
        alert_test = register_base_test(test,data.register_only_fill_all_except_confirmpassword)
        # check alert appear
        asserting.element_is_clickable_by_xpath(test,register_screen.error_input_confirm_password_xpath)
        # check alert text
        asserting.text_from_element_by_xpath(test,register_screen.error_input_confirm_password_xpath, alert_test)

    def test_010_register_only_fill_all_invalid_email(self):
        # start testcase
        test = functions.init_test_cases(sub_parent, 'Register Fill All with Invalid Email')
        # execute test
        alert_test = register_base_test(test,data.register_only_fill_all_invalid_email)
        # check alert appear
        asserting.element_is_clickable_by_xpath(test,register_screen.error_input_email_xpath)
        # check alert text
        asserting.text_from_element_by_xpath(test,register_screen.error_input_email_xpath, alert_test)
    
    def test_011_register_only_fill_all_not_match_password(self):
        # start testcase
        test = functions.init_test_cases(sub_parent, 'Register Fill All with Not Match Password')
        # execute test
        alert_test = register_base_test(test,data.register_only_fill_all_not_match_password)
        # check alert appear
        asserting.element_is_clickable_by_xpath(test,register_screen.error_input_confirm_password_xpath)
        # check alert text
        asserting.text_from_element_by_xpath(test,register_screen.error_input_confirm_password_xpath, alert_test)

    def test_012_register_only_fill_all_valid(self):
        # start testcase
        test = functions.init_test_cases(sub_parent, 'Register Fill All with Valid Value')
        # execute test
        alert_test = register_base_test(test,data.register_only_fill_all_valid)
        # check alert appear
        asserting.element_is_clickable_by_id(test,register_screen.success_register_id)
        # check alert text
        asserting.text_from_element_by_id(test,register_screen.success_register_id, alert_test)

    def test_013_register_only_fill_all_registered(self):
        # start testcase
        test = functions.init_test_cases(sub_parent, 'Register Fill All with Registered Email')
        # execute test
        alert_test = register_base_test(test,data.register_only_fill_all_registered)
        # check alert appear
        asserting.element_is_clickable_by_id(test,register_screen.error_failed_register_id)
        # check alert text
        asserting.text_from_element_by_id(test,register_screen.error_failed_register_id, alert_test)

    def test_999_ShutDownTest(self):
        # calling wrapper to end the test
        functions.extent_end_test(extent)


if __name__ == "__main__":
    unittest.main()