"""
This file contains all register contents for test cases
"""

# Test file and test class names
testFile = 'testfile'
testClass = 'MyTestSuite'

# List of test cases to be run
testCases = ["test_case"]

# Detailed information for each test case
testCases_details = {
    "test_case": {
        'tcScript': 'test_case',
        'testCaseName': 'Select Channel',
        'tcPurpose': 'To test the channel selection functionality',
        'tcDescription': "This test case verifies that the channel can be selected properly.",
        'test_data': {
            'config': {
                "url": 'http://example.com',
                "Username": "testuser",
                "password": "testpassword" 
            },
        }
    }
}
