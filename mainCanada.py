import os
import json
import platform
from time import sleep
from selenium import webdriver

info = None
with open('info.json', 'r') as f:
    info = json.load(f)

# Initialize the browser
chromeExePath = os.getcwd() + '/chromedriver'
if platform.system() == 'Windows':
    chromeExePath += '.exe'

browser = webdriver.Chrome(executable_path=chromeExePath)
browser.maximize_window()
browser.implicitly_wait(30)

# Used to create a url for the specific phone specs
def constructURL(capacity, color):
    # return 'https://www.apple.com/ca/shop/buy-iphone/iphone-8/4.7-inch-display-{}-{}'.format(capacity, color)
    return 'https://www.apple.com/ca/shop/buy-iphone/iphone-x/5.8-inch-display-{}-{}'.format(capacity, color)

browser.get(constructURL(info['Storage'], info['Color']))

print('Add to bag')
try:
    b = browser.find_element_by_xpath('//*[@id="main"]/store-provider/step1-modular/materializer/div[2]/div/summary-builder/div/div[2]/div[1]/div/div[1]/div/button')
except Exception:
    b = browser.find_element_by_xpath('//*[@id="main"]/store-provider/step1-modular/materializer/div[2]/div/summary-builder/div/div[2]/div[1]/div/div[1]/form/div/span/button')

sleep(1)
b.click()
print('Review bag')
browser.find_element_by_css_selector('#summaryheader-form > div > span > button').click()
print('Check out')
browser.find_element_by_css_selector('#cart-actions-checkout').click()
print('Adding email')
browser.find_element_by_css_selector('#login-appleId').send_keys(info['Email'])
print('Adding password')
browser.find_element_by_css_selector('#login-password').send_keys(info['Password'])
print('Signing in')
browser.find_element_by_css_selector('#sign-in').click()

sleep(0.2)
print('Continue')
browser.find_element_by_css_selector('#cart-continue-button').click()

sleep(1)
print('First name')
browser.find_element_by_css_selector('#shipping-user-firstName').send_keys(info['FirstName'])
print('Last name')
browser.find_element_by_css_selector('#shipping-user-lastName').send_keys(info['LastName'])
print('Area code')
browser.find_element_by_css_selector('#shipping-user-daytimePhoneAreaCode').send_keys(info['AreaCode'])
print('Primary phone')
browser.find_element_by_css_selector('#shipping-user-daytimePhone').send_keys(info['WirelessNumber'])
print('Street address')
browser.find_element_by_css_selector('#shipping-user-street').send_keys(info['Address1'])
print('Apt. Suite, Bldg.')
browser.find_element_by_css_selector('#shipping-user-street2').send_keys(info['Address2'])
print('Town/City')
browser.find_element_by_css_selector('#shipping-user-city').send_keys(info['City'])
print('Province')
browser.find_element_by_css_selector('#shipping-user-state').send_keys(info['Province'])
print('Postal code')
browser.find_element_by_css_selector('#shipping-user-postalCode').send_keys(info['PostalCode'])

sleep(0.2)
print('Continue')
browser.find_element_by_css_selector('#shipping-continue-button').click()

sleep(1)
print('Security Code')
browser.find_element_by_css_selector('#payment-credit-method-cc0-security-code').send_keys(info['SecurityCode'])
browser.find_element_by_css_selector('#payment-continue-button').click()

sleep(0.2)
print('Continue')
browser.find_element_by_css_selector('#payment-continue-button').click()

sleep(1)
print('Placing order...')
browser.find_element_by_css_selector('#place-order-button').click()
