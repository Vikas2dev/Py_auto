import logging
from selenium.common.exceptions import NoSuchElementException

class PageNavigation():
    """This class contains Selenium libraries for common operations"""
    
    def __init__(self, driver):
        self.driver = driver

    def get_url(self, url):
        """Opens the provided URL in the browser."""
        try:
            self.driver.get(url)
            logging.info(f"Opened URL: {url}")
        except Exception as e:
            logging.error(f"Failed to open URL: {url} with error: {e}")
            self.capture_screenshot()

    def back(self):
        """Navigates to the previous page."""
        try:
            self.driver.back()
            logging.info("Navigated back to the previous page.")
        except Exception as e:
            logging.error(f"Failed to navigate back with error: {e}")
            self.capture_screenshot()

    def forward(self):
        """Navigates to the next page."""
        try:
            self.driver.forward()
            logging.info("Navigated forward to the next page.")
        except Exception as e:
            logging.error(f"Failed to navigate forward with error: {e}")
            self.capture_screenshot()

    def refresh(self):
        """Refreshes the current page."""
        try:
            self.driver.refresh()
            logging.info("Refreshed the current page.")
        except Exception as e:
            logging.error(f"Failed to refresh the page with error: {e}")
            self.capture_screenshot()

    def capture_screenshot(self):
        """Captures a screenshot of the current page."""
        try:
            screenshot_path = 'screenshot.png'
            self.driver.save_screenshot(screenshot_path)
            logging.info(f"Screenshot saved to {screenshot_path}")
        except Exception as e:
            logging.error(f"Failed to capture screenshot with error: {e}")
