Mercury Tours Website Testing

A Selenium-based test automation suite for testing the Mercury Tours demo website (https://demo.guru99.com/test/newtours/).

Overview

This test suite covers three main testing scenarios:
1. User Registration
2. Login/Logout Functionality  
3. Flight Booking Process

Prerequisites

- Python 3.x
- Chrome browser
- Required Python packages:
  ```
  selenium
  webdriver-manager 
  unittest-xml-reporting
  ```

Installation

1. Clone this repository
2. Install dependencies:
```sh
pip install selenium webdriver-manager unittest-xml-reporting
```

Running Tests

Execute all tests and generate XML reports:

```sh
python testingNewTour.py
```

Test results will be saved in the [`test-reports`](test-reports ) directory as XML files.

Test Scenarios

1. Registration Tests
- Registration page loading
- Registration form field validation
- Successful registration flow
- Password mismatch validation
- Required fields validation

2. Login Tests
- Login page loading
- Successful login
- Failed login attempts
- Empty credentials validation
- Logout functionality

3. Flight Booking Tests
- Flight search page loading
- Form fields validation
- Round-trip flight search
- One-way flight search
- Empty search validation

Latest Test Results

- Total Tests: 15
- Passed: 13
- Failed: 2
- Errors: 0
- Skipped: 0

Failed tests:
- Empty login validation
- Required fields validation for registration

Project Structure

```
TestingTravelWebsite/
├── testingNewTour.py
├── test-reports/
│   ├── TEST-NewToursTest-20241004181507.xml
│   └── TEST-NewToursTest-20241004191202.xml
└── README.md
```
