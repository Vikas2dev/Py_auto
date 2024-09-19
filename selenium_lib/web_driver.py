import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options as f_options


class Driver(object):
    def __init__(self, browser_type, headless_mode=False):
        self.browser_type = browser_type
        self.headless_mode = headless_mode
        self.driver = None

    def get_driver(self):
        """ Getting driver instance"""
        try:
            logging.info(f'Opening {self.browser_type} browser..')

            if self.browser_type == 'CHROME':
                options = webdriver.ChromeOptions()
                desired_capabilities = DesiredCapabilities.CHROME
                window_size = "1920,1200"
                options.add_argument(f"--window-size={window_size}")
                options.add_argument('--incognito')
                options.add_argument('--dns-prefetch-disable')
                options.add_argument("--enable-javascript")
                options.add_argument('ignore-certificate-errors')
                
                if self.headless_mode:
                    options.add_argument("--headless")
                
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                desired_capabilities = options.to_capabilities()

                chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
                chromedriver_path = r"C:\Users\Dell\Favorites\Downloads\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe"
                options.binary_location = chrome_path
                
                # For Selenium 4.x: Use Service class
                #service = ChromeService(executable_path=chromedriver_path)
                #self.driver = webdriver.Chrome(service=service, options=options)
                
                # For Selenium 3.x: Comment the above two lines and uncomment below
                self.driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)

            elif self.browser_type == 'FIREFOX':
                desired_capabilities = DesiredCapabilities.FIREFOX
                firefox_profile = webdriver.FirefoxProfile()
                firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
                firefox_profile.set_preference("browser.download.folderList", 2)
                firefox_profile.set_preference("browser.download.dir", "/home/test/Downloads")
                firefox_profile.set_preference("browser.helperApps.neverAsk.saveToDisk",
                                               "application/octet-stream,application/pdf," \
                                               "application/csv,text/csv,text/plain")
                
                options = f_options()
                
                if self.headless_mode:
                    options.add_argument("-headless")

                gecko_driver_path = r"C:\path\to\geckodriver.exe"  # Update to your path
                
                # For Selenium 4.x: Use Service class
                service = FirefoxService(executable_path=gecko_driver_path)
                self.driver = webdriver.Firefox(service=service, firefox_profile=firefox_profile, options=options)
                
                # For Selenium 3.x: Comment the above two lines and uncomment below
                # self.driver = webdriver.Firefox(executable_path=gecko_driver_path, firefox_profile=firefox_profile, options=options)

            self.driver.implicitly_wait(15)
            self.driver.set_page_load_timeout(50)
            self.driver.delete_all_cookies()

            logging.info(f'{self.browser_type} browser opened successfully')
            return self.driver

        except Exception as ex:
            logging.critical(f"Exception {ex} occurred")
            return False
