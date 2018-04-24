#imos account creation

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

class AccountCreate(unittest.TestCase):

		# create driver
    def setUp(self):
        self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(30)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


		# close window.
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()





















