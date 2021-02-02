
from selenium.common.exceptions import NoSuchElementException
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_to_basket(browser):
    browser.get(link)
    try:
        btn = browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")
    except (NoSuchElementException):
        btn = False
    assert btn, "No button add to basket"
    
    