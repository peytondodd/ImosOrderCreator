

class LocationChecker():
    
    
        def AddressChecker(self):
            browser = self.browser
            # goes to this site
            browser.get(self.TRULIA_ADDRESS)
            street = browser.find_element_by_css_selector('dd.mbm')