from selenium import webdriver
from selenium.webdriver.common.keys import Keys

IMOS_DOMAIN = 'https://www.letsget.net/default.aspx?accountid=5438'
IMOS_ADDRESS = '133 Fiedler Ln'
IMOS_CITY = 'Fenton'
IMOS_ZIP = '63026'
IMOS_STATE = 'MO'
IMOS_PHONENUMBER = '6363493399'

REGISTER_ID = ('ctl00_BP_Content_lblRegisterNow')
LOGIN_ID = ('ctl00_BP_Content_lnkLogin')

def test_example():
    driver = webdriver.Firefox()
    driver.get(IMOS_DOMAIN)
	login = driver.find_element_by_name(LOGIN_ID).click()
	#driver.find_element_by_id(REGISTER_ID).click()

if __name__ == '__main__':
    test_example()