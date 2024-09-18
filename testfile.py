import unittest
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MyTestSuite(unittest.TestCase):

    def setUp(self):
        logging.info("Setting up the test environment")

    def tearDown(self):
        logging.info("Tearing down the test environment")

    def test_case_1(self):
        logging.info("Running test case 1")
        self.assertTrue(True)

    def test_case_2(self):
        logging.info("Running test case 2")
        self.assertTrue(True)

    def test_case_3(self):
        logging.info("Running test case 3")
        self.assertTrue(False)  # This will fail to show the log for failed tests

if __name__ == "__main__":
    unittest.main()
