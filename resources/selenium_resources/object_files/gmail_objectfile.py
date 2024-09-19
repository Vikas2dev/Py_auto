import logging
import time
from selenium_lib import selenium_methods
from selenium_lib import web_driver
from resources.selenium_resources.locaors import gmail_locators

class GmailSelenium:

    def __init__(self):
        self.driver = web_driver.Driver
        self.selHdl= selenium_methods.SeleniumCommonLib(self.driver)
    
    def gmail_signup(self, base_uri):
        if not self.driver.get_driver():
            return False
        if not self.selHdl.get_url(base_uri):
            return False
        if not self.selHdl.send_value(gmail_locators.first_name,"viharika",name="first name"):
            return False
        if not self.selHdl.send_value(gmail_locators.last_name,"aryan",name="last name"):
            return False
        if not self.selHdl.click_on_button(gmail_locators.name_next,name="next button"):
            return False
        if not self.selHdl.select_an_option_from_dropdown(gmail_locators.month,"May",name="month"):
            return False
        if not self.selHdl.send_value(gmail_locators.day, "11",name="day"):
            return False
        if not self.selHdl.send_value(gmail_locators.year, "1991",name="year"):
            return False
        if not self.selHdl.select_an_option_from_dropdown(gmail_locators.gender,"Female",name="gender"):
            return False
        if not self.selHdl.click_on_button(gmail_locators.gender_next,name="next button"):
            return False
        if not self.selHdl.click_on_button(gmail_locators.gmail_id,name="select gmail id"):
            return False
        if not self.selHdl.click_on_button(gmail_locators.id_next,name="next button"):
            return False
        if not self.selHdl.send_value(gmail_locators.password, "Varnika@123",name="password"):
            return False
        if not self.selHdl.send_value(gmail_locators.confirm_password, "Varnika@123",name="confirm password"):
            return False
        if not self.selHdl.click_on_button(gmail_locators.password_next,name="next button"):
            return False
        if not self.selHdl.send_value(gmail_locators.phone_number, "8123587894",name="phone number"):
            return False
        if not self.selHdl.click_on_button(gmail_locators.final_next,name="next button"):
            return False
        if not self.selHdl.click_on_button(gmail_locators.enter_otp,name="enter otp"):
            return False
        if not self.selHdl.click_on_button(gmail_locators.otp_next,name="next button"):
            return False       
        return True
