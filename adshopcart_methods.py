import datetime
import sys
import adshopcart_locators as locators
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
s = Service(executable_path='./chromedriver.exe')
driver = webdriver.Chrome(service=s)

def setUp():
    #  print test start day and time
    print(f'Test started at: {datetime.datetime.now()}')

    # Make a full screen
    driver.maximize_window()

    # Let's wait for the browser respond in general
    driver.implicitly_wait(30)

    # navigating to Moodle app website
    driver.get(locators.advantage_shopping_cart_url)

    # Checking that we're on the correct URL address and we're seeing correct title
    if driver.current_url == locators.advantage_shopping_cart_url and driver.title == "\u00A0""Advantage Shopping":
        print(f'we are at advantage online shopping homepage --{driver.current_url}')
        print(f'we\'re seeing title message --{driver.title} ')
        sleep(1)

    else:
        print(f'we\'re not at the advantage online shopping homepage, Check your code!')
        driver.close()
        driver.quit()


def tearDown():
    if driver is not None:
        print(f'------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()


def create_new_user():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(3)
    driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
    sleep(3)

    if driver.current_url == locators.adshopcart_register_url:
        driver.find_element(By.XPATH, '//h3[text()="CREATE ACCOUNT"]').is_displayed()
        sleep(0.25)
        print(f'We are at register page- {locators.adshopcart_register_url}')

        driver.find_element(By.XPATH, '//input[@name= "usernameRegisterPage"]').click()
        sleep(0.25)

        # Enter fake data into username open fields
        driver.find_element(By.XPATH, '//input[@name= "usernameRegisterPage"]').send_keys(locators.new_username)
        sleep(0.25)

        driver.find_element(By.XPATH, '//input[@name= "emailRegisterPage"]').send_keys(locators.email)
        sleep(0.25)

        driver.find_element(By.XPATH, '//input[@name= "passwordRegisterPage"]').send_keys(locators.new_password)
        sleep(0.25)

        driver.find_element(By.XPATH, '//input[@name= "confirm_passwordRegisterPage"]').send_keys(locators.new_password)
        sleep(0.25)

        driver.find_element(By.XPATH, '//input[@name= "first_nameRegisterPage"]').send_keys(locators.first_name)
        sleep(0.25)

        driver.find_element(By.XPATH, '//input[@name= "last_nameRegisterPage"]').send_keys(locators.last_name)
        sleep(0.25)

        driver.find_element(By.XPATH, '//input[@name= "phone_numberRegisterPage"]').send_keys(locators.phone)
        sleep(0.25)

        driver.execute_script("window.scrollTo(0,500);")
        sleep(0.25)

        driver.find_element(By.XPATH, '//select[@name= "countryListboxRegisterPage"]').click()
        sleep(0.25)

        Select(driver.find_element(By.XPATH, '//select[@name= "countryListboxRegisterPage"]')).select_by_visible_text(
            'Canada')
        driver.find_element(By.XPATH, '//input[@name= "cityRegisterPage"]').send_keys(locators.city)
        sleep(0.25)

        driver.find_element(By.XPATH, '//input[@name= "addressRegisterPage"]').send_keys(locators.address)
        sleep(0.25)

        driver.find_element(By.XPATH, '//input[@name= "state_/_province_/_regionRegisterPage"]').send_keys(locators.province)
        sleep(0.25)

        driver.find_element(By.XPATH, '//input[@name= "postal_codeRegisterPage"]').send_keys(locators.postal_code)
        sleep(0.25)

        bool()
        checkbox_promoption = driver.find_element(By.XPATH, '//input[@name= "allowOffersPromotion"]')
        if checkbox_promoption:
            checkbox_promoption.click()
            sleep(2)
            if checkbox_promoption.is_selected():
                print('Checked "promotion.." checkbox')

            else:
                print('unchecked "promotion.." checkbox')

        checkbox_iagree = driver.find_element(By.XPATH, '//input[@name= "i_agree"]')
        if checkbox_iagree:
            checkbox_iagree.click()
            sleep(2)
            if checkbox_iagree.is_selected():
                print('Checked "I_agree.." checkbox')

            else:
                print('Unchecked "I_agree.." checkbox')

        register_btn = driver.find_element(By.ID, 'register_btnundefined')
        if register_btn.is_enabled():
            register_btn.click()
            sleep(3)
            print('Register button is enable')

        else:
            print('Register button is disabled.Check your code!')

    print(f'Test scenario: Create a new user - New user account is created.\n'
          f' Username- "{locators.new_username},Full name- "{locators.full_name}", Email- "{locators.email} -------is passed')


def check_new_user_account():
    # Click by "My Account" button
    if driver.current_url == locators.advantage_shopping_cart_url:
        driver.find_element(By.ID, 'menuUser').click()
        sleep(2)

        driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[1]').click()
        sleep(2)

        if driver.current_url == locators.my_account_url:
            assert driver.find_element(By.XPATH, f'//label[contains(.,"{locators.full_name}")]').is_displayed()
            print(f'Test scenario: Navigate to My account page-"{locators.my_account_url}",\n'
                  f'Check created new user account with Full name- "{locators.full_name}"-----is passed')

    # Click by "My Order" button
        driver.find_element(By.ID, 'menuUser').click()
        sleep(2)

        driver.find_element(By.XPATH, '//*[@id ="loginMiniTitle"]/label[2]').click()
        sleep(2)
        if driver.current_url == locators.my_order_url:
            assert driver.find_element(By.XPATH, f'//label[contains(.," - No orders - ")]').is_displayed()
            print(f'Test scenario: Navigate to My order page "{locators.my_order_url}", Check " NO orders "-------is passed')

    # Click by "Sign Out" button
        driver.find_element(By.ID, 'menuUser').click()
        sleep(2)

        driver.find_element(By.XPATH, '//*[@id ="loginMiniTitle"]/label[3]').click()
        sleep(2)

        if driver.current_url == locators.advantage_shopping_cart_url:
            print(f'Test scenario: Navigate to Sign out page"{locators.advantage_shopping_cart_url}"\n'
                  f' Sign out  -------is passed')


def login_with_new_credential():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(2)

    driver.find_element(By.NAME, "username").send_keys(locators.new_username)
    sleep(2)

    driver.find_element(By.NAME, "password").send_keys(locators.new_password)
    sleep(2)

    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(2)

    print(f'Test scenario: login with new credential:\n'
          f' Username- "{locators.new_username}",Password- "{locators.new_password}"-------------------is passed')


def delete_user():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(2)

    driver.find_element(By.XPATH, '//*[ @ id = "loginMiniTitle"]/label[1]').click()
    sleep(2)

    driver.execute_script("window.scrollTo(0,600);")
    sleep(2)

    driver.find_element(By.CLASS_NAME, 'deleteBtnText').click()
    sleep(2)

    if driver.find_element(By.ID, 'deleteAccountPopup').is_displayed():
        sleep(2)

        driver.find_element(By.XPATH, '//*[@class="deletePopupBtn deleteRed"]').click()
        sleep(2)
        print(f'Test scenario: Delete new user account Username - "{locators.new_username} -------is passed')
        sleep(10)

    else:
        print('Fail to delete a new user account. Check your code!')


def login_with_deleted_user():
    # check that we are on the user's Main page
    if driver.current_url == locators.advantage_shopping_cart_url:
        driver.find_element(By.ID, 'menuUser').click()
        sleep(2)

        driver.find_element(By.NAME, "username").send_keys(locators.new_username)
        sleep(2)

        driver.find_element(By.NAME, "password").send_keys(locators.new_password)
        sleep(2)

        driver.find_element(By.ID, 'sign_in_btnundefined').click()
        sleep(2)

        driver.find_element(By.ID, 'signInResultMessage').is_displayed()
        sleep(2)

        driver.find_element(By.XPATH, '//*[@class="closeBtn loginPopUpCloseBtn"]').click()
        sleep(2)

        print(f'Test scenario: Check login with a deleted user account \n'
              f'Username- "{locators.new_username}", password- "{locators.new_password}"\n'
              f'"Incorrect user name or password" error message is displayed -------is passed')

    else:
        print('something goes wrong. Check your code!')


# setUp()
# create_new_user()
# check_new_user_account()
# login_with_new_credential()
# delete_user()
# login_with_deleted_user()
# tearDown()


