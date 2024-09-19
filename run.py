import unittest
import os
import logging
import time

# Configure logging
log_file_path = os.path.join('logs', 'test_suite.log')
if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(filename=log_file_path,
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def run_tests_with_details():
    """
    Runs the provided test cases with detailed logging of names, purposes, and steps.
    """
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    # Log test case details
    logging.info("Adding test case - Name: {details.get('testCaseName', 'Unnamed')}")
    time.sleep(1)  # Delay before the next log
    testFile = 'testfile'
    testClass = 'MyTestSuite'
    # Load the test case from the specified test file and classtes
    suite.addTests(loader.loadTestsFromTestCase(getattr(__import__(testFile), testClass)))
    
    logging.info("Starting the test suite with selected test cases")
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    logging.info(f"Total tests run: {result.testsRun}")
    logging.info(f"Failures: {len(result.failures)}")
    logging.info(f"Errors: {len(result.errors)}")
    time.sleep(1)  # Delay before logging completion
    logging.info("Test suite completed.")

if __name__ == "__main__":
    run_tests_with_details()
