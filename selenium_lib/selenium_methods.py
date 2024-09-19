import time
import logging
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from datetime import datetime
class SeleniumCommonLib():
    """This class contains selenium libraries"""
    def __init__(self, driver):
        self.driver = driver

    def clear_and_send_value(self, xpath, value, name='', mask=False, press_enter=False):
        """This method first clear the input field and sending keys
        """
        try:
            if self.is_element_displayed(xpath, name):
                element = self.driver.find_element_by_xpath(xpath)
                element.clear()
                print(logging.INFO, f"Cleared the '{name}'")
                self.wait_time(1)
                element.send_keys(value)
                if mask:
                    value = len(value)*'*'
                print(
                    logging.INFO, f"Entered '{value}' to the '{name}'")
                if press_enter:
                    element.send_keys(Keys.ENTER)
                return True
            return False

        except NoSuchElementException:
            print(
                logging.ERROR, "Send value to input field has issue. Please check")
            self.capture_screenshot()
            return False

    def is_element_displayed(self, xpath, name=''):
        """This method check whether element is displyed or not
        """
        try:
            if self.driver.find_element_by_xpath(xpath).is_displayed():
                print(
                    logging.INFO, f"The Element '{name}' does exist")
                return True
            print(
                logging.INFO, f"The Element '{name}' does not exist")
            return False

        except NoSuchElementException:
            print(
                logging.ERROR, f"The Element '{name}' does not exist")
            self.capture_screenshot()
            return False

    def send_value(self, xpath, value, name='', mask=False):
        """This method send value to input field
        """
        try:
            if self.is_element_displayed(xpath, name):
                self.driver.find_element_by_xpath(xpath).send_keys(value)
                if not mask:
                    print(
                        logging.INFO, f"Entered '{value}' to the '{name} input'")
                else:
                    print(
                        logging.INFO, f"Entered '{len(value)*'*'}' to the '{name}'")
                return True
            return False

        except NoSuchElementException:
            print(
                logging.ERROR, "Send value to input field has issue.Please check")
            self.capture_screenshot()
            return False

    def click_on_button(self, xpath, name='', timeout=10):
        """This method is click on the button.
        """
        try:
            if not self.is_element_present(xpath, name,timeout):
                return False
            element = self.driver.find_element_by_xpath(xpath)
            element.click()
            self.wait_time(2)
            print(logging.DEBUG, "Clicked on button")
            print(
                logging.INFO, f"clicked on {name} button")
            return True

        except NoSuchElementException:
            print(
                logging.ERROR, f"The Element '{name}' does not exist")
            self.capture_screenshot()
            return False

        except Exception as ex:
            log = "Failed to click element :: exception %s" % ex
            print(
                logging.ERROR, log)
            self.capture_screenshot()
            return False

    def click_on_element(self, xpath, name='',timeout=10):
        """This method is used to click on element.
        """
        try:
            if not self.is_element_present(xpath, name, timeout):
                return False
            element = self.driver.find_element_by_xpath(xpath)
            print(logging.DEBUG, f"{name} element exist")
            element.click()
            self.wait_time(2)
            print(logging.DEBUG, "Clicked on element")
            print(
                logging.INFO, f"clicked on {name} element")
            return True

        except Exception as ex:
            log = "Failed to click element :: exception %s" % ex
            print(
                logging.ERROR, log)
            self.capture_screenshot()
            return False


    def select_radio_button(self, locator, radio_button_name):
        """This method enable radio button if not enabled.
        """
        try:
            if self.is_enable_element(locator, radio_button_name):
                self.driver.find_element_by_xpath(locator).click()
                self.wait_time(1)
            return True

        except Exception as ex:
            msg = 'Not able to select the radio button %s:: ' \
                  'An Exception occured %s ' % (radio_button_name, ex)
            print(logging.ERROR, msg)
            self.capture_screenshot()
            return False

    def is_enable_element(self, xpath, name=''):
        """This method verify button is enabled or not.
        """
        try:
            if not self.driver.find_element_by_xpath(xpath).is_enabled():
                lprint(
                    logging.ERROR, "'%s' Element is not enable. Please check" % name)
                return False
            print(logging.INFO, "'%s' element is enabled" % name)
            return True

        except NoSuchElementException:
            print(
                logging.ERROR,'Element enabling took too much time')
            return False

    def is_clickable(self, xpath, name=''):
        """This method verify button is clickable or not.
        """
        try:
            if not WebDriverWait(self.driver, 15).until(
                    EC.element_to_be_clickable((By.XPATH, xpath))):
                print(logging.INFO, f"Element {name} is not clickable")
                self.capture_screenshot()
                return False
            return True

        except TimeoutException:
            print(
                    logging.ERROR, f"Loading took too much time to check {name} " \
                                   f"element is clickable")
            self.capture_screenshot()
            return False

        except NoSuchElementException:
            print(
                logging.ERROR, 'Element is not present. Please check')
            self.capture_screenshot()
            return False

    def get_current_url(self):
        """This method Returns Current URL
           of the web-page
        """
        text_value = self.driver.current_url
        if not text_value:
            self.ph_handler.lprint(
                logging.ERROR, "Current URL does not have value. Please check")
            return False
        return text_value

def capture_screenshot(self):
    """This method saves the screenshot."""
    try:
        # Define the test case name and file name directly
        test_case_name = "YourTestCaseName"  # You should provide the actual test case name here
        file_name = f"{test_case_name}-{datetime.now().strftime('%H-%M-%S')}"

        # Logging and printing the screenshot saving process
        logging.info(f"Saving Screenshot as {file_name}.png")
        print(f"Saving Screenshot as {file_name}.png")

        # Define the log file path (update the path according to your project structure)
        log_file_path = "/logs"  # Provide the actual path
        path = f"{log_file_path}/{file_name}.png"
        self.driver.save_screenshot(path)

        # Logging and printing the screenshot path
        logging.info(f"Screenshot path :: {path}")
        print(f"Screenshot path :: {path}")
        
        return True

    except Exception as ex:
        # Handling the exception with logging and printing
        msg = f"save screenshot failed :: An Exception occurred {ex}"
        logging.error(msg)
        print(msg)
        
        return False

    def wait_time(self, wait_in_seconds):
        """This method used to wait some seconds
        """
        #self.ph_handler.sleep(wait_in_seconds)
        time.sleep(wait_in_seconds)

    def refresh_page(self, sleep_time=2):
        """This method used to refresh page
        """
        self.ph_handler.lprint(logging.INFO, 'Refreshing page..')
        self.driver.refresh()
        self.ph_handler.sleep(sleep_time)

    def open_url(self, url, new_tab=False):
        """This method used to browse url.
        """
        try:
            if new_tab:
                self.ph_handler.lprint(logging.INFO, f'Creating new tab..')
                self.driver.execute_script("window.open()")
                self.ph_handler.lprint(logging.INFO, f'Successfully created new tab.')
                self.ph_handler.lprint(logging.INFO, f'Switching to new window..')
                handles = self.driver.window_handles
                self.driver.switch_to.window(handles[-1])
                self.ph_handler.lprint(logging.INFO, f'Successfully switched to  new tab.')
            self.driver.get(url)
            self.ph_handler.lprint(logging.INFO, f'Opening url : "{url}"')
            self.wait_time(2)
            return True

        except Exception as ex:
            msg = 'navigate url failed :: An Exception occured %s ' % ex
            self.ph_handler.lprint(logging.ERROR,msg)
            self.capture_screenshot()
            return False

    def is_present(self, xpath, name='', error_log =True):
        """This method verify xpath present or not.
        """
        try:
            self.driver.find_element_by_xpath(xpath)
            self.ph_handler.lprint(
                logging.INFO, f"'{name}' Element is present.")
            return True

        except NoSuchElementException:
            if error_log == 'INFO':
                self.ph_handler.lprint(logging.INFO, f"Element '{name}' not present.")
            elif error_log:
                self.ph_handler.lprint(logging.ERROR, f"Element '{name}' not present.")
                self.capture_screenshot()
            return False

    def is_element_present(self, xpath, name='', error_log =True, timeout=10):
        """This method verify element present or not.
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath)))
            self.ph_handler.lprint(logging.INFO, f"Element {name} is present")
            return True

        except TimeoutException:
            if error_log:
                self.ph_handler.lprint(
                        logging.ERROR, f'Took too much time to locate {name} element')
                self.capture_screenshot()
            return False

    def get_element_text(self, xpath, name='', flag=False):
        """ This method print the element text if present"""
        try:
            text_value = self.driver.find_element_by_xpath(xpath).text
            if not text_value:
                self.ph_handler.lprint(logging.INFO, "web element does not have value.Please check")
                return None
            return text_value

        except NoSuchElementException:
            if flag:
                return False
            self.ph_handler.lprint(
                 logging.ERROR,f"Element '{name}' not present.")
            self.capture_screenshot()
            return False


    def is_checkbox_selected(self,xpath, name):
        """ This method check checbox is selected or not"""
        try:
            if self.driver.find_element_by_xpath(xpath).is_selected():
                self.ph_handler.lprint(
                    logging.INFO, f"{name} checkbox is selected")
                return True
            else:
                self.ph_handler.lprint(
                    logging.INFO, f"{name} checkbox is not selected")
                return False

        except Exception as ex:
            log = "failed fetching if checkbox is selected or not. %s"%ex
            self.ph_handler.lprint(logging.ERROR, log)
            self.capture_screenshot()
            return False

    def check_repeatation_element_exists_by_xpath(self, xpath):
        """This method returns number of elements present for provided xpath"""
        try:
            repeatation = len(self.driver.find_elements_by_xpath(xpath))
            self.ph_handler.lprint(logging.INFO, "The element exists for %s times" % repeatation)
            return repeatation

        except NoSuchElementException:
            self.ph_handler.lprint(logging.ERROR, "The element does not exist. Please check!!")
            return False

    def toast_msg(self, xpath="", wait_time=10):
        """This method fetch toast massage"""
        try:
            if not xpath:
                xpath="//*[@class='toast-message']"
            close_button = "//div[@class='v-snack__action ']/button"
            WebDriverWait(self.driver, wait_time).until(
                        EC.presence_of_element_located((By.XPATH, xpath)))
            self.wait_time(2)
            toast_message = self.get_element_text(xpath, 'toast_message', True)
            if toast_message:
                self.ph_handler.lprint(logging.INFO, f"toast message :: {toast_message}")
                try:
                    if self.driver.find_element_by_xpath(close_button).click():
                        self.ph_handler.lprint(logging.INFO, "Clicked on Close button")
                        self.wait_time(1)
                except Exception as ex:
                   self.ph_handler.lprint(logging.INFO, "Close button not present may toast message " \
                                                        "disapeared.")
                return toast_message
            self.ph_handler.lprint(logging.INFO, "There is no toast message found.")
            return False

        #except TimeoutException:
        except Exception as ex:
            self.ph_handler.lprint(
                    logging.ERROR, f"Loading took too much time locate toast message. Please check!!")
            return False

    def scroll_page(self, flag ='up'):
        """This method used to scroll page"""
        if flag == 'up':
            self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        elif flag == 'down':
            self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.END)
        return True

    def scroll_into_view(self, xpath):
        """This method used to scroll to element"""
        try:
            flag = self.driver.find_element_by_xpath(xpath)
            self.driver.execute_script("arguments[0].scrollIntoView();", flag)
            return True

        except Exception as ex:
            log = 'The element does not exist. Please check!!. %s' % ex
            self.ph_handler.lprint(logging.ERROR, log)
            return False

    def get_attribute_of_an_element(self, xpath, attribute_name):
        """This method used to get the attribute"""
        try:
            attribute_value = self.driver.find_element_by_xpath(xpath).get_attribute(attribute_name)
            if attribute_value is not None:
                return attribute_value
            else:
                self.ph_handler.lprint(logging.INFO, "Attribute value is None.")
                return None

        except Exception as ex:
            log = 'Failed getting attribute from xpath. %s' % ex
            self.ph_handler.lprint(logging.ERROR, log)
            return False

        
    def select_and_send_value(self, xpath, value, name='', mask=False, press_enter=True):
        """This method first select and input field and sending keys
        """
        try:
            if self.is_element_displayed(xpath, name):
                element = self.driver.find_element_by_xpath(xpath)
                element.send_keys(Keys.CONTROL, 'a')
                self.wait_time(1)
                element.send_keys(value)
                self.wait_time(1)
                if press_enter:
                    element.send_keys(Keys.ENTER)
                if mask:
                    value = len(value)*'*'
                self.ph_handler.lprint(
                    logging.INFO, f"Entered '{value}' to the '{name}'")
                return True
            return False

        except NoSuchElementException:
            self.ph_handler.lprint(
                logging.ERROR, "Send value to input field has issue. Please check")
            self.capture_screenshot()
            return False

    def explicit_wait(self, locator_value, locator='XPATH', time_out=10):
        """This method wait untill xpath availablity for the given time out
        """
        try:
            if locator=='XPATH':
                WebDriverWait(self.driver, time_out).until(
                        EC.presence_of_element_located((By.XPATH, locator_value)))
                return True

        except Exception as ex:
            log = 'The element does not exist. Please check!!. %s' % ex
            self.ph_handler.lprint(logging.ERROR, log)
            self.capture_screenshot()
            return False

    def move_to_element_using_action_chains(self, xpath, name=''):
        """This method used to move mouse cursore to provided xpath location
        """
        try:
            action = ActionChains(self.driver)
            action_element = self.driver.find_element_by_xpath(xpath)
            action.move_to_element(action_element).perform()
            self.wait_time(2)
            self.ph_handler.lprint(logging.INFO, f"successfully move to the element {name}")
            return True

        except Exception as ex:
            log = "failed to perform move action. %s" % ex
            self.ph_handler.lprint(logging.ERROR,log)
            self.capture_screenshot()
            return False

    def send_value_to_dropdown(self, xpath, value, name=''):
        """This method send value to input field
        """
        try:
            if self.is_element_displayed(xpath, name):
                self.driver.find_element_by_xpath(xpath).send_keys(value)
                self.ph_handler.lprint(
                    logging.INFO, f"Entered '{value}' to the '{name} dropdown'")
                return True
            return False

        except NoSuchElementException:
            self.ph_handler.lprint(
                logging.ERROR, "Send value to dropdown has issue.Please check")
            self.capture_screenshot()
            return False

    def expand_search_select_value_in_dropdown(self, expand_xpath, value_xpath, value, name=''):
        """This method send value to input field
        """
        try:
            if self.is_element_displayed(expand_xpath, name):
                self.driver.find_element_by_xpath(value_xpath).send_keys(value)
                self.ph_handler.lprint(
                    logging.INFO, f"Entered '{value}' to the '{name} dropdown'")
                if self.click_on_element(value_xpath, name):
                    return True
            return False

        except NoSuchElementException:
            self.ph_handler.lprint(
                logging.ERROR, "Send value to dropdown has issue.Please check")
            self.capture_screenshot()
            return False

    def get_element_options(self, xpath):
        """This method returns the list of value from options"""
        try:
            list_elements = self.driver.find_elements_by_xpath(xpath)
            options = []
            for option in list_elements:
                options.append(option.text)
            return options

        except NoSuchElementException:
            self.ph_handler.lprint(logging.ERROR, "The element does not exist.Please check!!")
            return False

    def send_value_to_dropdown_and_select(self, field_xpath, value, value_xpath, name=''):
        """This method send value to dropdown and select element
        """
        try:
            if not self.select_and_send_value(field_xpath, value, name, press_enter=False):
                return False
            if self.click_on_element(value_xpath, name):
                return True
            return False

        except NoSuchElementException:
            self.ph_handler.lprint(
                logging.ERROR, "Send value to dropdown has issue.Please check")
            self.capture_screenshot()
            return False
 
    def select_value_from_dropown(self, xpath, value, name='', select_method=None):
        """This method used to select value from the dropdown
           select_methods = 'select by value', select_by_visible_text, select_by_index
           default is select_by_visible_text
        """
        try:
            sel = Select(self.driver.find_element_by_xpath(xpath))
            if select_method == 'by_index':
                sel.select_by_index(value)
                print(logging.INFO, f"successfully selected index {value} value")
            elif select_method == 'select by value':
                sel.select_by_value(value)
                print(logging.INFO, f"successfully selected value {value}")
            else:
                sel.select_by_visible_text(value)
                print(logging.INFO, f"successfully selected the visible text {value}")
            return True

        except Exception as ex:
            log = "failed to select the value from dropdown. %s" % ex
            print(logging.ERROR,log)
            self.capture_screenshot()
            return False