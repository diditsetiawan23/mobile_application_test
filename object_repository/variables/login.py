# Assert text
error_email_text = 'Enter Valid Email'
error_password_text = 'Enter Valid Password'
error_login_text = 'Wrong Email or Password'
valid_email = 'test@automation.com'
valid_password = '12345678'
invalid_email = 'not_registered@automation.com'
invalid_password = 'sdfsefewfwefewfweew'
not_valid_email = 'mot_valid_email'

base_data = {
    "email":"",
    "password":"",
    "assertText":""
}


login_without_email_and_password = base_data.copy()
login_without_email_and_password["email"] = ""
login_without_email_and_password["password"] = ""
login_without_email_and_password["assertText"] = error_email_text 

login_without_password = base_data.copy()
login_without_password["email"] = valid_email
login_without_password["password"] = ""
login_without_password["assertText"] = error_password_text 

login_without_email = base_data.copy()
login_without_email["email"] = ""
login_without_email["password"] = valid_password
login_without_email["assertText"] = error_password_text 

login_with_notvalid_email = base_data.copy()
login_with_notvalid_email["email"] = not_valid_email
login_with_notvalid_email["password"] = valid_password
login_with_notvalid_email["assertText"] = error_email_text 

login_with_unregistered_email = base_data.copy()
login_with_unregistered_email["email"] = invalid_email
login_with_unregistered_email["password"] = invalid_password
login_with_unregistered_email["assertText"] = error_password_text 

login_with_nomatch_email_password = base_data.copy()
login_with_nomatch_email_password["email"] = valid_email
login_with_nomatch_email_password["password"] = invalid_password
login_with_nomatch_email_password["assertText"] = error_login_text

login_with_valid_email_password = base_data.copy()
login_with_valid_email_password["email"] = valid_email
login_with_valid_email_password["password"] = valid_password
login_with_valid_email_password["assertText"] = "" 


