# run_tests.py
import unittest
import os
from testfile import MyTestSuite
from testsuites import test_cases  
import unittest
import logging
import unittest
import logging
import time
import logging
import time
import unittest

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configure logging to file
log_file_path = os.path.join('logs', 'test_suite.log')
logging.basicConfig(filename=log_file_path,
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
def run_tests_with_details(test_cases):
    """
    Runs the provided test cases with detailed logging of names, purposes, and steps.
    """
    suite = unittest.TestSuite()

    for test_name, test_details in test_cases.items():
        logging.info(f"Adding {test_name} - Purpose: {test_details['purpose']}")
        time.sleep(1)  # Delay before the next log
        logging.info(f"Steps: {', '.join(test_details['steps'])}")
        time.sleep(1)  # Delay before adding the test to the suite
        suite.addTest(MyTestSuite(test_name))

    logging.info("Starting the test suite with selected test cases")
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    logging.info(f"Total tests run: {result.testsRun}")
    logging.info(f"Failures: {len(result.failures)}")
    logging.info(f"Errors: {len(result.errors)}")
    time.sleep(1)  # Delay before logging completion
    logging.info("Test suite completed.")

if __name__ == "__main__":
    run_tests_with_details(test_cases)
