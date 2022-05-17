from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
#from time import sleep (пункт 2 из критериев проверки)

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_existance(browser):
    browser.get(link)
    #sleep(30)
    try:
        browser.find_element(By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    except NoSuchElementException:
        return False
    return True



