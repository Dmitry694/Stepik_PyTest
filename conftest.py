import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    if user_language != None:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language= - not selected language, website support:"
                          "\nca - Català"
                          "\ncs - Cesky"
                          "\nda - Dansk"
                          "\nde - Deutsch"
                          "\nen-gb - British-Enlish"
                          "\nel - Ελληνικά"
                          "\nes - Español"
                          "\nfi - Suomi"
                          "\nfr - Français"
                          "\nit - Italiano"
                          "\nko - 한국어"
                          "\nnl - Nederlands"
                          "\npl - Polski"
                          "\npt - Português"
                          "\npt-br - Português-Brasileiro"
                          "\nro - Română"
                          "\nru - Русский"
                          "\nsk - Slovensky"
                          "\nuk - Українська"
                          "\nzh-hans - 简体中文"
                          "\nar - Arabian")
    yield browser
    print("\nquit browser..")
    browser.quit()