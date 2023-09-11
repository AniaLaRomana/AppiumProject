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

    def test_registration_1_0_blank_fields(self):
        # LOCATORS for the Welcome to Headspace page
        continueWithEmail = "com.getsomeheadspace.android:id/continueWithEmailButton"  # id

        # LOCATORS for the Sign Up page
        signUpPageTitle = "com.getsomeheadspace.android:id/titleTextView"  # id
        isThePasswordCorrect = "//android.widget.ImageView[@index='1']"  # xpath

        # TEST DATA
        # all fields are left blank


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
                                    "/TC1_0_SingUpPageConfirmation.png")

        # saving a comment about the status of the executed step
        log.info("Took the TC_1_0_SingUpPageConfirmation screenshot")
        log.info("Sing Up page opened")

        # locating the isThePasswordCorrect indicator and checking if the password is correct or not
        try:
            element = self.driver.find_element(AppiumBy.XPATH, isThePasswordCorrect)
            self.assertFalse(element.is_displayed())
        except:
            # taking a screenshot and saving a comment about the status of the executed step
            log.info("Password is not correct, an account cannot be created")
            self.driver.save_screenshot("C:/Users/shade/PycharmProjects/pythonProject/AppiumProject/screenshots"
                                        "/TC1_0_PasswordCheck.png")
            log.info("Took the TC_1_0_PasswordCheck screenshot")
        else:
            # taking a screenshot and saving a comment about the status of the executed step
            log.info("Password is correct, an account can be created")
            self.driver.save_screenshot("C:/Users/shade/PycharmProjects/pythonProject/AppiumProject/screenshots"
                                        "/TC1_0_PasswordCheck.png")
            log.info("Took the TC_1_0_PasswordCheck screenshot")
            assert False
        finally:
            # saving a comment about the status of the executed step
            log.info("TC_registration_1_0 is completed")

if __name__ == '__main__':
    unittest.main()
