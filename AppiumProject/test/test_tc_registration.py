import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from customLogger.custom_logger import customLogger as cl


class RegistrationTest(unittest.TestCase):

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
            # saving a comment about the status of the executed step
            log.info("Password is not correct, an account cannot be created")
        finally:
            # taking a screenshot and saving a comment about the status of the executed step
            log.info("Password is not correct, an account cannot be created")
            self.driver.save_screenshot("C:/Users/shade/PycharmProjects/pythonProject/AppiumProject/screenshots"
                                        "/TC1_0_PasswordCheck.png")
            log.info("Took the TC_1_0_PasswordCheck screenshot")

    def test_registration_1_1_passwordContaining_1upperCaseCharacter_lowerCaseCharacters_1number_1specialCharacter(self):
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
        firstNameValue = "Sheldon"
        lastNameValue = "Cooper"
        emailAddressValue = "sc@imaginary.com"
        passwordValue = "P@sswor1"

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
                                    "/TC1_1_SingUpPageConfirmation.png")
        # saving a comment about the status of the executed step
        log.info("Took the TC_1_1_SingUpPageConfirmation screenshot")
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
            assert False
        else:
            self.assertTrue(element.is_displayed())
            # saving a comment about the status of the executed step
            log.info("Password is correct, an account can be created")
        finally:
            # taking a screenshot and saving a comment about the status of the executed step
            self.driver.save_screenshot("C:/Users/shade/PycharmProjects/pythonProject/AppiumProject/screenshots"
                                        "/TC1_1_PasswordCheck.png")
            log.info("Took the TC_1_1_PasswordCheck screenshot")


    def test_registration_1_2_passwordContaining_1upperCaseCharacter_lowerCaseCharacters_1number(self):
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
        emailAddressValue = "hw@blabla.com"
        firstNameValue = "Howard"
        lastNameValue = "Wolowitz"
        passwordValue = "Passwor1"

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
                                    "/TC1_2_SingUpPageConfirmation.png")
        # saving a comment about the status of the executed step
        log.info("Took the TC_1_2_SingUpPageConfirmation screenshot")
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
            assert False
        else:
            self.assertTrue(element.is_displayed())
            # saving a comment about the status of the executed step
            log.info("Password is correct, an account can be created")
        finally:
            # taking a screenshot and saving a comment about the status of the executed step
            self.driver.save_screenshot("C:/Users/shade/PycharmProjects/pythonProject/AppiumProject/screenshots"
                                        "/TC1_2_PasswordCheck.png")
            log.info("Took the TC_1_2_PasswordCheck screenshot")

    def test_registration_1_3_passwordContaining_1upperCaseCharacter_lowerCaseCharacters_1specialCharacter(self):
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
        emailAddressValue = "leonard@hofstadter.pl"
        firstNameValue = "Leonard"
        lastNameValue = "Hofstadter"
        passwordValue = "P@ssword"

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
                                    "/TC1_3_SingUpPageConfirmation.png")

        # saving a comment about the status of the executed step
        log.info("Took the TC_1_3_SingUpPageConfirmation screenshot")
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
            assert False
        else:
            self.assertTrue(element.is_displayed())
            # saving a comment about the status of the executed step
            log.info("Password is correct, an account can be created")
        finally:
            # taking a screenshot and saving a comment about the status of the executed step
            self.driver.save_screenshot("C:/Users/shade/PycharmProjects/pythonProject/AppiumProject/screenshots"
                                        "/TC1_3_PasswordCheck.png")
            log.info("Took the TC_1_3_PasswordCheck screenshot")

    def test_registration_1_4_passwordContaining_lowerCaseCharacters_1number_1specialCharacter(self):

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
            assert False
        else:
            self.assertTrue(element.is_displayed())
            # saving a comment about the status of the executed step
            log.info("Password is correct, an account can be created")
        finally:
            # taking a screenshot and saving a comment about the status of the executed step
            self.driver.save_screenshot("C:/Users/shade/PycharmProjects/pythonProject/AppiumProject/screenshots"
                                        "/TC1_4_PasswordCheck.png")
            log.info("Took the TC_1_4_PasswordCheck screenshot")

    def test_registration_1_5_passwordContaining_upperCaseCharacters_1number_1specialCharacter(self):
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
        emailAddressValue = "rajesh@imaginary.in"
        firstNameValue = "Rajesh"
        lastNameValue = "Koothrappali"
        passwordValue = "P@SSWOR1"

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
                                    "/TC1_5_SingUpPageConfirmation.png")

        # saving a comment about the status of the executed step
        log.info("Took the TC_1_5_SingUpPageConfirmation screenshot")
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
            assert False
        else:
            self.assertTrue(element.is_displayed())
            # saving a comment about the status of the executed step
            log.info("Password is correct, an account can be created")
        finally:
            # taking a screenshot and saving a comment about the status of the executed step
            self.driver.save_screenshot("C:/Users/shade/PycharmProjects/pythonProject/AppiumProject/screenshots"
                                        "/TC1_5_PasswordCheck.png")
            log.info("Took the TC_1_5_PasswordCheck screenshot")

    def test_registration_1_6_too_short_password(self):
        # LOCATORS for the Welcome to Headspace page
        continueWithEmail = "com.getsomeheadspace.android:id/continueWithEmailButton"  # id

        # LOCATORS for the Sign Up page
        signUpPageTitle = "com.getsomeheadspace.android:id/titleTextView"  # id
        firstName = "com.getsomeheadspace.android:id/firstNameEditText"  # id
        lastName = "com.getsomeheadspace.android:id/lastNameEditText"  # id
        emailAddress = "com.getsomeheadspace.android:id/emailEditText"  # id
        password = "com.getsomeheadspace.android:id/passwordEditText"  # id
        isThePasswordCorrect = "//android.widget.ImageView[@index='1']"  #xpath

        # TEST DATA
        emailAddressValue = "bmaryann@rost.com"
        firstNameValue = "Bernadette Mary Ann"
        lastNameValue = "Rostenkowski"
        passwordValue = "P@sswo1"


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
                                    "/TC1_6_SingUpPageConfirmation.png")

        # saving a comment about the status of the executed step
        log.info("Took the TC_1_6_SingUpPageConfirmation screenshot")
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
            self.assertFalse(element.is_displayed())
        except:
            # saving a comment about the status of the executed step
            log.info("Password is not correct, an account cannot be created")
        finally:
            # taking a screenshot and saving a comment about the status of the executed step
            self.driver.save_screenshot("C:/Users/shade/PycharmProjects/pythonProject/AppiumProject/screenshots"
                                        "/TC1_6_PasswordCheck.png")
            log.info("Took the TC_1_6_PasswordCheck screenshot")

if __name__ == '__main__':
    unittest.main()
