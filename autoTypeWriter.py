from costantFile import *
from splinter import Browser

def main():
    browser = Browser('chrome')
    driver = browser.driver

    automaticTyping(browser, driver, S_LINK_TYPINGTEST_PAGE)

    driver.implicitly_wait(10)
    browser.quit()


def automaticTyping(browser, driver, stringLinkPage):
    browser.visit(stringLinkPage)

    clickBtnFromId(browser, POLICY_BTN_TYPING_PAGE_SETTINGS)
    clickBtnFromId(browser, POLICY_BTN_TYPING_PAGE_SAVE)
    clickListOfBtnFromID(browser, LIST_OF_ID_TO_BE_REMOVED)
    
    automaticFillTheInput(browser, driver, ELEMENTS_TO_BE_WRITTEN, FORM_TO_WRITE_ID)

def automaticFillTheInput(browser, driver, XPath, formId):
    wordsList = browser.find_by_xpath(XPath)
    inputField = browser.find_by_id(formId) 
    driver.implicitly_wait(3)
    for word in wordsList:
        inputField.fill(word.value)
        inputField.type(' ')

def clickListOfBtnFromID(browser, btnList):
    for btnId in btnList:
        clickBtnFromId(browser, btnId)

def clickBtnFromId(browser, btnPolicyId):
    policyBtn = browser.find_by_id(btnPolicyId)
    if len(policyBtn)!=0:
        policyBtn.first.click()   

main()
