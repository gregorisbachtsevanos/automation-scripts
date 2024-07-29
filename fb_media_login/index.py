from selenium import webdriver

driver = webdriver.Firefox()
driver.get(“https://www.facebook.com/")

# Find the email or phone field and enter the email or phone number
email_field = driver.find_element_by_id(“email”)
email_field.send_keys(“your_email_or_phone”)

# Find the password field and enter the password
password_field = driver.find_element_by_id(“pass”)
password_field.send_keys(“your_password”)

# Find the login button and click it
login_button = driver.find_element_by_id(“loginbutton”)
login_button.click()
