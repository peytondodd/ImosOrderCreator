from selenium import webdriver
from selenium.webdriver.common.keys import Keys

IMOS_DOMAIN = 'https://www.letsget.net/default.aspx?accountid=5438'

def test_example():
    driver = webdriver.Firefox()
    driver.get(IMOS_DOMAIN)


if __name__ == '__main__':
    test_example()