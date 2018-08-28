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
browser.implicitly_wait(20)

# Used to create a url for the specific phone specs
def constructURL(capacity, color, carrier):
    # return 'https://www.apple.com/shop/buy-iphone/iphone-8/4.7-inch-display-{}-{}-{}'.format(capacity, color, carrier)
    return 'https://www.apple.com/shop/buy-iphone/iphone-x/5.8-inch-display-{}-{}-{}'.format(capacity, color, carrier)

browser.get(constructURL(info['Storage'], info['Color'], info['Carrier']))

contButton = browser.find_element_by_css_selector('#main > store-provider > step1-modular > materializer.rs-step1modular-sheet.rs-purchasesummary.ase-materializer.ase-materializer-show > div.rs-purchasesummary-background > div > summary-builder > div > div.row.rs-purchasesummary-actionbox > div.large-5.large-push-7.small-12.small-push-0.column > div > div.as-purchaseinfo-button.grouped-button-left > div > button')
contButton.send_keys('\n')

sleep(1)
f = browser.find_element_by_css_selector('#fullPrice-description')
browser.execute_script("arguments[0].click();", f)

# Find the button to go to activate the phone
try:
    contButton = browser.find_element_by_css_selector('#main > store-provider > step1-modular > materializer.rs-step1modular-sheet.rs-purchasesummary.ase-materializer.ase-materializer-show > div.rs-purchasesummary-background > div > summary-builder > div > div.row.rs-purchasesummary-actionbox > div.large-5.large-push-7.small-12.small-push-0.column > div > div.as-purchaseinfo-button.grouped-button-left > div > button')
    sleep(0.5)
except Exception:
    contButton = browser.find_element_by_css_selector('#main > store-provider > step1-modular > materializer.rs-step1modular-sheet.rs-purchasesummary.ase-materializer.ase-materializer-show > div.rs-purchasesummary-background > div > summary-builder > div > div.row.rs-purchasesummary-actionbox > div.large-5.large-push-7.small-12.small-push-0.column > div > div.as-purchaseinfo-button.grouped-button-left > form > div > span > button')
    sleep(0.5)

browser.execute_script("window.scrollTo(0, -document.body.scrollHeight/2);")
contButton.click()

# Don't enter any mobile information for tmobile users, because it is not needed
if info['Carrier'] != 'tmobile':
    # Enter the information in the input fields then continue
    browser.find_element_by_css_selector('#upgrade-eligibility-ctn').send_keys(info['AreaCode'] + info['WirelessNumber'])
    if info['Carrier'] == 'sprint':
        browser.find_element_by_css_selector('#upgrade-eligibility-ssn').send_keys(info['AccountPin'])
    elif info['Carrier'] == 'att' or info['Carrier'] == 'verizon':
        browser.find_element_by_css_selector('#upgrade-eligibility-postal-code').send_keys(info['BillingZip'])
        browser.find_element_by_css_selector('#upgrade-eligibility-ssn').send_keys(info['SSN'])

    browser.find_element_by_css_selector('#preauth-button-next').click()

    # Wait until the phone is activated, then press continue
    sleep(1)
    while True:
        b = browser.find_element_by_css_selector('#preauth-button-next') 
        if b.is_displayed():
            b.click()
            break

# Go to cart
sleep(1)
browser.find_element_by_css_selector('#summaryheader-form > div > span > button').click()

# Press checkout button
browser.find_element_by_css_selector('#cart-actions-checkout').click()

# Enter apple account information
browser.find_element_by_css_selector('#login-appleId').send_keys(info['Email'])
browser.find_element_by_css_selector('#login-password').send_keys(info['Password'])
# Login
browser.find_element_by_css_selector('#sign-in').click()

# Buy the iphone
browser.find_element_by_css_selector('#cart-continue-button').click()
sleep(1)

browser.find_element_by_css_selector('#shipping-user-firstName').send_keys(info['FirstName'])
browser.find_element_by_css_selector('#shipping-user-lastName').send_keys(info['LastName'])
browser.find_element_by_css_selector('#shipping-user-daytimePhoneAreaCode').send_keys(info['AreaCode'])
browser.find_element_by_css_selector('#shipping-user-daytimePhone').send_keys(info['WirelessNumber'])
browser.find_element_by_css_selector('#shipping-user-street').send_keys(info['Address1'])
browser.find_element_by_css_selector('#shipping-user-street2').send_keys(info['Address2'])

postal = browser.find_element_by_css_selector('#shipping-user-postalCode')
postal.clear()
postal.send_keys(info['BillingZip'])
sleep(1.5)

browser.find_element_by_css_selector('#shipping-continue-button').click()
sleep(1)
browser.find_element_by_css_selector('#payment-credit-method-cc0-security-code').send_keys(info['SecurityCode'])
browser.find_element_by_css_selector('#payment-continue-button').click()
sleep(1)

if info['Carrier'] != 'tmobile':
    browser.find_element_by_css_selector('#terms-accept').click()
    sleep(0.5)
    browser.find_element_by_css_selector('#terms-continue-button').click()

sleep(1)
browser.find_element_by_css_selector('#place-order-button').click()
