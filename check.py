from selenium import webdriver
from selenium.webdriver.common.keys import Keys



WAIT_TIME = '5'

REGISTER = ('https://www.letsget.net/(S(jggjirci2tdctkj20ivzf4j5))/Public/CustomerRegistration.aspx')
LOGIN_ID = ('ctl00_BP_Content_lnkLogin')

def register():
    driver = webdriver.Firefox()
    driver.get(REGISTER)

def account_create():
	driver = webdriver.Firefox()
    driver.find_element_by_id('ctl00_BP_Content_uLoginInfo_txtEmailAddress').send_keys(IMOS_CITY) 
   
if __name__ == '__main__':
    register()
	account_create()
	
