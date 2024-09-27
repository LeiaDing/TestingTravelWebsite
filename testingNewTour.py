import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import xmlrunner


class NewToursTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demo.guru99.com/test/newtours/")
        self.driver.maximize_window()
    
    def tearDown(self):
        self.driver.quit()
    
    # Scenario 1: Registration
    def test_registration_page_load(self):
        self.driver.find_element(By.LINK_TEXT, "REGISTER").click()
        self.assertTrue("Register: Mercury Tours" in self.driver.title)
    
    def test_registration_form_fields(self):
        self.driver.find_element(By.LINK_TEXT, "REGISTER").click()
        fields = ["firstName", "lastName", "phone", "userName", "address1", "city", "state", "postalCode", "country", "email", "password", "confirmPassword"]
        for field in fields:
            self.assertTrue(self.driver.find_element(By.NAME, field).is_displayed())
    
    def test_successful_registration(self):
        self.driver.find_element(By.LINK_TEXT, "REGISTER").click()
        self.driver.find_element(By.NAME, "firstName").send_keys("John")
        self.driver.find_element(By.NAME, "lastName").send_keys("Doe")
        self.driver.find_element(By.NAME, "phone").send_keys("1234567890")
        self.driver.find_element(By.NAME, "userName").send_keys("johndoe@example.com")
        self.driver.find_element(By.NAME, "address1").send_keys("123 Test St")
        self.driver.find_element(By.NAME, "city").send_keys("Test City")
        self.driver.find_element(By.NAME, "state").send_keys("Test State")
        self.driver.find_element(By.NAME, "postalCode").send_keys("12345")
        self.driver.find_element(By.NAME, "country").send_keys("UNITED STATES")
        self.driver.find_element(By.NAME, "email").send_keys("johndoe")
        self.driver.find_element(By.NAME, "password").send_keys("password123")
        self.driver.find_element(By.NAME, "confirmPassword").send_keys("password123")
        self.driver.find_element(By.NAME, "submit").click()
        self.assertTrue("Thank you for registering" in self.driver.page_source)
    
    def test_registration_password_mismatch(self):
        self.driver.find_element(By.LINK_TEXT, "REGISTER").click()
        self.driver.find_element(By.NAME, "firstName").send_keys("John")
        self.driver.find_element(By.NAME, "lastName").send_keys("Doe")
        self.driver.find_element(By.NAME, "phone").send_keys("1234567890")
        self.driver.find_element(By.NAME, "userName").send_keys("johndoe@example.com")
        self.driver.find_element(By.NAME, "address1").send_keys("123 Test St")
        self.driver.find_element(By.NAME, "city").send_keys("Test City")
        self.driver.find_element(By.NAME, "state").send_keys("Test State")
        self.driver.find_element(By.NAME, "postalCode").send_keys("12345")
        self.driver.find_element(By.NAME, "country").send_keys("UNITED STATES")
        self.driver.find_element(By.NAME, "email").send_keys("johndoe")
        self.driver.find_element(By.NAME, "password").send_keys("password123")
        self.driver.find_element(By.NAME, "confirmPassword").send_keys("password321")
        self.driver.find_element(By.NAME, "submit").click()
        self.assertTrue("PAssword and con" not in self.driver.page_source)
    
    def test_registration_required_fields(self):
        self.driver.find_element(By.LINK_TEXT, "REGISTER").click()
        self.driver.find_element(By.NAME, "submit").click()
        self.assertTrue("Thank you for registering" not in self.driver.page_source)
    
    # Scenario 2: Login
    def test_login_page_load(self):
        self.assertTrue("Welcome: Mercury Tours" in self.driver.title)
    
    def test_successful_login(self):
        self.driver.find_element(By.NAME, "userName").send_keys("johndoe")
        self.driver.find_element(By.NAME, "password").send_keys("password123")
        self.driver.find_element(By.NAME, "submit").click()
        self.assertTrue("Login Successfully" in self.driver.page_source)
    
    def test_failed_login(self):
        self.driver.find_element(By.NAME, "userName").send_keys("wronguser")
        self.driver.find_element(By.NAME, "password").send_keys("wrongpassword")
        self.driver.find_element(By.NAME, "submit").click()
        self.assertTrue("Enter your userName and password correct" in self.driver.page_source)
    
    def test_empty_login(self):
        self.driver.find_element(By.NAME, "submit").click()
        self.assertTrue("Enter your userName and password correct" in self.driver.page_source)
    
    def test_logout(self):
        self.driver.find_element(By.NAME, "userName").send_keys("johndoe")
        self.driver.find_element(By.NAME, "password").send_keys("password123")
        self.driver.find_element(By.NAME, "submit").click()
        self.driver.find_element(By.LINK_TEXT, "SIGN-OFF").click()
        self.assertTrue("Welcome: Mercury Tours" in self.driver.title)
    
    # Scenario 3: Flight Booking
    def test_flight_page_load(self):
        self.driver.find_element(By.LINK_TEXT, "Flights").click()
        self.assertTrue("Find a Flight: Mercury Tours:" in self.driver.title)
    
    def test_flight_search_form_fields(self):
        self.driver.find_element(By.LINK_TEXT, "Flights").click()
        fields = ["tripType", "passCount", "fromPort", "fromMonth", "fromDay", "toPort", "toMonth", "toDay", "servClass", "airline"]
        for field in fields:
            self.assertTrue(self.driver.find_element(By.NAME, field).is_displayed())
    
    def test_flight_search(self):
        self.driver.find_element(By.LINK_TEXT, "Flights").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[value='roundtrip']").click()
        self.driver.find_element(By.NAME, "passCount").send_keys("2")
        self.driver.find_element(By.NAME, "fromPort").send_keys("London")
        self.driver.find_element(By.NAME, "fromMonth").send_keys("July")
        self.driver.find_element(By.NAME, "fromDay").send_keys("15")
        self.driver.find_element(By.NAME, "toPort").send_keys("New York")
        self.driver.find_element(By.NAME, "toMonth").send_keys("August")
        self.driver.find_element(By.NAME, "toDay").send_keys("15")
        self.driver.find_element(By.CSS_SELECTOR, "input[value='First']").click()
        self.driver.find_element(By.NAME, "findFlights").click()
        self.assertTrue("After flight finder - No Seats Avaialble" in self.driver.page_source)
    
    def test_one_way_flight_search(self):
        self.driver.find_element(By.LINK_TEXT, "Flights").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[value='oneway']").click()
        self.driver.find_element(By.NAME, "passCount").send_keys("1")
        self.driver.find_element(By.NAME, "fromPort").send_keys("New York")
        self.driver.find_element(By.NAME, "fromMonth").send_keys("December")
        self.driver.find_element(By.NAME, "fromDay").send_keys("25")
        self.driver.find_element(By.NAME, "toPort").send_keys("London")
        self.driver.find_element(By.CSS_SELECTOR, "input[value='Business']").click()
        self.driver.find_element(By.NAME, "findFlights").click()
        self.assertTrue("After flight finder - No Seats Avaialble" in self.driver.page_source)
    
    def test_flight_search_no_selection(self):
        self.driver.find_element(By.LINK_TEXT, "Flights").click()
        self.driver.find_element(By.NAME, "findFlights").click()
        self.assertTrue("After flight finder - No Seats Avaialble" in self.driver.page_source)

if __name__ == "__main__":
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        # these make sure that some options that are not applicable
        # remain hidden from the help menu.
        failfast=False, buffer=False, catchbreak=False)