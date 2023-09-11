import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from customLogger.custom_logger import customLogger as cl


class RegistrationTests(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '13'
        desired_caps['deviceName'] = 'eSMART'
        desired_caps['appPackage'] = 'com.getsomeheadspace.android'
        desired_caps['appActivity'] = '.splash.SplashActivity'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['uiautomator2ServerLaunchTimeout'] = 200000
        desired_caps['uiautomator2ServerInstallTimeout'] = 200000
        desired_caps['appWaitForLaunch'] = 'false'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True

        localAppiumUrl = 'http://127.0.0.1:4723/wd/hub'

        # initializing the WebDriver
        self.driver = webdriver.Remote(localAppiumUrl, desired_caps)

        # creating the object for the Custom Logger class
        log = cl()

        # saving a comment about the status of the executed step
        log.info("Launched the app")

    def tearDown(self):
        self.driver.quit()

    def test_registration_1_4_valid_test_data(self):

        # LOCATORS for the Welcome to Headspace page
        continueWithEmail = "com.getsomeheadspace.android:id/continueWithEmailButton"  # id

        # LOCATORS for the Sign Up page
        signUpPageTitle = "com.getsomeheadspace.android:id/titleTextView"  # id
        firstName = "com.getsomeheadspace.android:id/firstNameEditText"  # id
        lastName = "com.getsomeheadspace.android:id/lastNameEditText"  # id
        emailAddress = "com.getsomeheadspace.android:id/emailEditText"  # id
        password = "com.getsomeheadspace.android:id/passwordEditText"  # id
        isThePasswordCorrect = "//android.widget.ImageView[@index='1']"  # xpath

        # TEST DATA
        emailAddressValue = "penny@hof.com"
        firstNameValue = "Penny"
        lastNameValue = "Hofstadter"
        passwordValue = "p@sswor1"

        # setting the implicitly wait for 35s
        self.driver.implicitly_wait(35)

        # locating the "Continue with email" button
        element = self.driver.find_element(AppiumBy.ID, continueWithEmail)

        # cliking the "Continue with email" button
        element.click()

        # creating the object for the Custom Logger class
        log = cl()

        # saving a comment about the status of the executed step
        log.info("Clicked the Continue with email button")

        # checking if clicking the "Continue with email" button redirected to the Sign Up page
        element = self.driver.find_element(AppiumBy.ID, signUpPageTitle)
        self.assertTrue(element.is_displayed())

        # taking a screenshot
        self.driver.save_screenshot("C:/Users/shade/PycharmProjects/pythonProject/AppiumProject/screenshots"
                                    "/TC1_4_SingUpPageConfirmation.png")

        # saving a comment about the status of the executed step
        log.info("Took the TC_1_4_SingUpPageConfirmation screenshot")
        log.info("Sing Up page opened")

        # locating the first name field
        element = self.driver.find_element(AppiumBy.ID, firstName)

        # clicking the first name field
        element.click()

        # saving a comment about the status of the executed step
        log.info("Clicked the First name field")

        # entering the first name
        element.send_keys(firstNameValue)

        # saving a comment about the status of the executed step
        log.info("First name entered")

        # locating the last name field
        element = self.driver.find_element(AppiumBy.ID, lastName)

        # clicking the last name field
        element.click()

        # saving a comment about the status of the executed step
        log.info("Clicked the Last name field")

        # entering the last name
        element.send_keys(lastNameValue)

        # saving a comment about the status of the executed step
        log.info("Last name entered")

        # locating the email address field
        element = self.driver.find_element(AppiumBy.ID, emailAddress)

        # clicking the email address field
        element.click()

        # saving a comment about the status of the executed step
        log.info("Clicked the Email address field")

        # entering the email address
        element.send_keys(emailAddressValue)

        # saving a comment about the status of the executed step
        log.info("Email address entered")

        # locating the password field
        element = self.driver.find_element(AppiumBy.ID, password)

        # clicking the password field
        element.click()

        # saving a comment about the status of the executed step
        log.info("Clicked the Password field")

        # entering the password
        element.send_keys(passwordValue)

        # saving a comment about the status of the executed step
        log.info("Password entered")

        # locating the isThePasswordCorrect indicator and checking if the password is correct or not
        try:
            element = self.driver.find_element(AppiumBy.XPATH, isThePasswordCorrect)
        except:
            # taking a screenshot and saving a comment about the status of the executed step
            log.info("Password is not correct, an account cannot be created")
            self.driver.save_screenshot("C:/Users/shade/PycharmProjects/pythonProject/AppiumProject/screenshots"
                                        "/TC1_4_PasswordCheck.png")
            log.info("Took the TC_1_4_PasswordCheck screenshot")
            assert False
        else:
            self.assertTrue(element.is_displayed())
            # taking a screenshot and saving a comment about the status of the executed step
            log.info("Password is correct, an account can be created")
            self.driver.save_screenshot("C:/Users/shade/PycharmProjects/pythonProject/AppiumProject/screenshots"
                                        "/TC1_4_PasswordCheck.png")
            log.info("Took the TC_1_4_PasswordCheck screenshot")
        finally:
            # saving a comment about the status of the executed step
            log.info("TC_registration_1_4 is completed")


if __name__ == '__main__':
    unittest.main()