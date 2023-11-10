error_name_text = 'Enter Full Name'
error_email_text = 'Enter Valid Email'
error_password1_text = 'Enter Password'
error_password2_text = 'Password Does Not Matches'
error_registered_text = 'Email Already Exists'
success_register_text = 'Registration Successful'
name = "Automation Test"
valid_email = 'test@automation.com'
valid_password = '12345678'
invalid_email = 'not_registered@automation.com'
invalid_password = 'invalid_password'
not_valid_email = 'mot_valid_email'

base_data = {
    "name":"",
    "email":"",
    "password":"",
    "pass_confirm":"",
    "assertText":""
}

register_without_fill_all_data = base_data.copy()
register_without_fill_all_data["assertText"] = error_name_text

register_only_fill_name = base_data.copy()
register_only_fill_name["name"] = name
register_only_fill_name["assertText"] = error_email_text

register_only_fill_email = base_data.copy()
register_only_fill_email["email"] = valid_email
register_only_fill_email["assertText"] = error_name_text

register_only_fill_password = base_data.copy()
register_only_fill_password["password"] = valid_password
register_only_fill_password["assertText"] = error_name_text

register_only_fill_confirmpassword = base_data.copy()
register_only_fill_confirmpassword["pass_confirm"] = valid_password
register_only_fill_confirmpassword["assertText"] = error_name_text

register_fill_all_except_name = base_data.copy()
register_fill_all_except_name["email"] = valid_email
register_fill_all_except_name["password"] = valid_password
register_fill_all_except_name["pass_confirm"] = valid_password
register_fill_all_except_name["assertText"] = error_name_text

register_only_fill_all_except_email = base_data.copy()
register_only_fill_all_except_email["name"] = name
register_only_fill_all_except_email["password"] = valid_password
register_only_fill_all_except_email["pass_confirm"] = valid_password
register_only_fill_all_except_email["assertText"] = error_email_text

register_only_fill_all_except_password = base_data.copy()
register_only_fill_all_except_password["name"] = name
register_only_fill_all_except_password["email"] = valid_email
register_only_fill_all_except_password["pass_confirm"] = valid_password
register_only_fill_all_except_password["assertText"] = error_password1_text

register_only_fill_all_except_confirmpassword = base_data.copy()
register_only_fill_all_except_confirmpassword["name"] = name
register_only_fill_all_except_confirmpassword["email"] = valid_email
register_only_fill_all_except_confirmpassword["password"] = valid_password
register_only_fill_all_except_confirmpassword["assertText"] = error_password2_text

register_only_fill_all_invalid_email = base_data.copy()
register_only_fill_all_invalid_email["name"] = name
register_only_fill_all_invalid_email["email"] = not_valid_email
register_only_fill_all_invalid_email["password"] = valid_password
register_only_fill_all_invalid_email["pass_confirm"] = valid_password
register_only_fill_all_invalid_email["assertText"] = error_email_text

register_only_fill_all_not_match_password = base_data.copy()
register_only_fill_all_not_match_password["name"] = name
register_only_fill_all_not_match_password["email"] = valid_email
register_only_fill_all_not_match_password["password"] = valid_password
register_only_fill_all_not_match_password["pass_confirm"] = invalid_password
register_only_fill_all_not_match_password["assertText"] = error_password2_text

register_only_fill_all_valid = base_data.copy()
register_only_fill_all_valid["name"] = name
register_only_fill_all_valid["email"] = valid_email
register_only_fill_all_valid["password"] = valid_password
register_only_fill_all_valid["pass_confirm"] = valid_password
register_only_fill_all_valid["assertText"] = success_register_text

register_only_fill_all_registered = base_data.copy()
register_only_fill_all_registered["name"] = name
register_only_fill_all_registered["email"] = valid_email
register_only_fill_all_registered["password"] = valid_password
register_only_fill_all_registered["pass_confirm"] = valid_password
register_only_fill_all_registered["assertText"] = error_registered_text

