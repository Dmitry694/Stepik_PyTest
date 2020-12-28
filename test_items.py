import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_check_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)
    btn_add_to_basket = browser.find_elements_by_css_selector('#add_to_basket_form > button')
    assert btn_add_to_basket, f'Добавить в коризну отсутствует ({link})'