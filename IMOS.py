# NOTES:
#       Use trulia to check address in fenton/imperial and put available address in a .text list 
#       the list that trulia creates will be the same list imos.py will pull address from to use to make
#       deliverys.
#
#        
#
#
#
#


import sys
from random import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

class IMOS(unittest.TestCase):


##################################
#        ACOUNT CREATION
##################################
    def random_email(self, length):
        return ''.join(random.sample([string.ascii_lowercase, string.ascii_uppercase],  1) for i in range(length)) + random.sample(["@gmail.com", "@icloud.com", "@yahoo.com", "@mail.com", "@firefoxmail.com"],  1)

    def random_password(self, length):
        return ''.join(random.sample([string.ascii_lowercase, string.ascii_uppercase],  1) for i in range(length)) + random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],  4)

    def random_firstname(self):
        fname = open('firstname.txt').read().splitlines()
        return random.choice(fname)
  
    def random_lastname(self):
        lname = open('lastname.txt').read().splitlines()
        return random.choice(lname)

    def random_phonenumber(self):
        return random.sample([314, 636],  1) + random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],  3) + random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],  4)

##################################
#        ADDRESS CREATION
##################################

        
##################################
#        PIZZA CREATER
##################################
    def random_pizza(self):
        kind = random.sample([1,2,3,4,5,6,7],1)
        return random.sample([self.PIZZA_CHEESE,self.DELUXE,self.PIZZA_VEGGIE,self.PIZZA_ALLMEAT,self.PIZZA_BBQ, self.PIZZA_EGG, self.PIZZA_RANDOM],  kind)
        
        # random_pizza_size
    def random_pizza_size(self):
        sizee = random.sample([1,2,3,4],1)
        return random.sample([self.PIZZA_SIZE_10,self.SIZE_12,self.PIZZA_SIZE_14,self.PIZZA_SIZE_16], sizee)
        
    def random_toppings(self): 
        tops = random.sample([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],1)
        return random.sample([self.PIZZA_TOPPINGS_CHEESE,self.PIZZA_TOPPINGS_SAUSAGE,
        self.PIZZA_TOPPINGS_PEPPERONI,self.PIZZA_TOPPINGS_BACON,self.PIZZA_TOPPINGS_HAMBURGER,
        self.PIZZA_TOPPINGS_CANADIANBACON,self.PIZZA_TOPPINGS_CHICKEN,self.PIZZA_TOPPINGS_ANCHOVY,
        self.PIZZA_TOPPINGS_MUCHROOM,self.PIZZA_TOPPINGS_ONION,self.PIZZA_TOPPINGS_GREENPEPPER,
        self.PIZZA_TOPPINGS_BLACKOLIVE,self.PIZZA_TOPPINGS_TOMATO,self.PIZZA_TOPPINGS_PINEAPPLE,
        self.PIZZA_TOPPINGS_JALAPENO, self.PIZZA_TOPPINGS_PEPPERONCINI,self.PIZZA_TOPPINGS_SHRIMP], tops)
        
    def random_extra_toppings(self):
        extops = random.sample([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],1)
        return random.sample([self.PIZZA_TOPPINGS_CHEESE,self.PIZZA_TOPPINGS_SAUSAGE,
        self.PIZZA_TOPPINGS_PEPPERONI,self.PIZZA_TOPPINGS_BACON,self.PIZZA_TOPPINGS_HAMBURGER,
        self.PIZZA_TOPPINGS_CANADIANBACON,self.PIZZA_TOPPINGS_CHICKEN,self.PIZZA_TOPPINGS_ANCHOVY,
        self.PIZZA_TOPPINGS_MUCHROOM,self.PIZZA_TOPPINGS_ONION,self.PIZZA_TOPPINGS_GREENPEPPER,
        self.PIZZA_TOPPINGS_BLACKOLIVE,self.PIZZA_TOPPINGS_TOMATO,self.PIZZA_TOPPINGS_PINEAPPLE,
        self.PIZZA_TOPPINGS_JALAPENO, self.PIZZA_TOPPINGS_PEPPERONCINI,self.PIZZA_TOPPINGS_SHRIMP], extops) 
    
    def random_special_toppins(self):
        special = random.sample([1,2,3,4,5,6,7,8,9],1)
        return random.sample([self.PIZZA_SPECIAL_LIGHTCHEESE,self.PIZZA_SPECIAL_NOCHEESE,
        self.PIZZA_SPECIAL_WELLDONE,self.PIZZA_SPECIAL_HALFBAKED,self.PIZZA_SPECIAL_DONOTCUT,
        self.PIZZA_SPECIAL_THICKERCRUST,self.PIZZA_SPECIAL_NOSAUCE,self.PIZZA_SPECIAL_LIGHTSAUCE,
        self.PIZZA_SPECIAL_EXTRASAUCE], special) 

    def random_typed_notes(self):
        notes = open('notes.txt').read().splitlines()
        return random.choice(notes)
        
    def random_sidedips(self):
        dips = random.sample([1,2,3,4],1)
        return random.sample([self.PIZZA_SIDE_REDPEPPER,self.PIZZA_SIDE_PARMESANCHEESE,
                            self.PIZZA_SIDE_IMOSHOUSEDRESSING,self.PIZZA_SIDE_SIDERANCHDRESSING], dips) 
             
    
##################################
#        SHORTCUTS
##################################
    def setupboi(self):
        self.browser = webdriver.Firefox()
        
        #Imos Infoz
        self.IMOS_DOMAIN = 'https://www.letsget.net/default.aspx?accountid=5438'
        self.IMOS_PIZZA = 'https://www.imospizza.com/'
        self.IMOS_FENTON = 'https://www.imospizza.com/location/restaurant/fenton-mo'
        self.IMOS_LOCATION = 'https://www.imospizza.com/find-a-location'
        self.IMOS_ADDRESS = '133 Fiedler Ln'
        self.IMOS_CITY = 'Fenton'
        self.IMOS_ZIP = '63026'
        self.IMOS_STATE = 'MO'
        self.IMOS_PHONENUMBER = '6363493399'
        
        #Account Create
        self.EMAIL = random_email(9) # 9 = total letter length
        self.PASSWORD = random_password(7) # 7 = letter total length
        self.PASSWORDCONFIRM = self.PASSWORD # pulls from orginal password
        self.PASSWORDHINT = self.PASSWORD # pulls from orginal password
        self.FIRSTNAME = random_firstname()
        self.LASTNAME = random_lastname()
        self.ZIPCODE = 63026 
        
        #IDs
        self.REGISTER_ID = ('ctl00_BP_Content_lblRegisterNow')
        self.LOGIN_ID = ('ctl00_BP_Content_lnkLogin')
        
        self.EMAIL_ID = ('ctl00_BP_Content_uLoginInfo_txtEmailAddress')
        self.PASSWORD_ID = ('ctl00_BP_Content_uLoginInfo_txtPassword')
        self.PASSWORDCONFIM_ID = ('ctl00_BP_Content_uLoginInfo_txtConfirmPassword')
        self.PASSWORDHINT_ID = ('ctl00_BP_Content_uLoginInfo_txtPasswordHint')
        self.FIRSTNAME_ID = ('ctl00_BP_Content_txtFirstName')
        self.LASTNAME_ID = ('ctl00_BP_Content_txtLastName')
        self.ZIPCODE_ID = ('ctl00_BP_Content_txtZipCode_txt') 
        self.AGECONFIRM_ID = ('ctl00_BP_Content_chkOver13')

        #Buttons
         # register screen button to create account
        self.REGISTER_BUTTON = ('ctl00_BP_Content_ubtnRegister_btnAction')
         # next button used when selecting delivery or pickup.
        self.DELIVERY_NEXT_BUTTON = ('ctl00_BP_Content_ubtnNext_btnAction')
                            
        # Pizza Types
        self.PIZZA_CHEESE = ('ctl00_BP_Content_img699397')
        self.PIZZA_DELUXE = ('ctl00_BP_Content_img699399')
        self.PIZZA_VEGGIE = ('ctl00_BP_Content_img699401')
        self.PIZZA_ALLMEAT = ('ctl00_BP_Content_img699403')
        self.PIZZA_BBQ = ('ctl00_BP_Content_img699476')
        self.PIZZA_EGG = ('ctl00_BP_Content_img702738')
        # choose your own toppings
        self.PIZZA_RANDOM = ('ctl00_BP_Content_img699393')
        
        self.PIZZA_SIZE_10 = ('ctl00_BP_Content_uOrderOptionSets_rptOrderOptionSets_ctl00_rblItems_297009')
        self.PIZZA_SIZE_12 = ('ctl00_BP_Content_uOrderOptionSets_rptOrderOptionSets_ctl00_rblItems_297018')
        self.PIZZA_SIZE_14 = ('ctl00_BP_Content_uOrderOptionSets_rptOrderOptionSets_ctl00_rblItems_297027')
        self.PIZZA_SIZE_16 = ('ctl00_BP_Content_uOrderOptionSets_rptOrderOptionSets_ctl00_rblItems_297036')
        
        self.PIZZA_TOPPINGS_CHEESE = ('ctl00_BP_Content_uOrderOptionSets_rptOrderOptionSets_ctl02_rblItems_1216640')
        self.PIZZA_TOPPINGS_SAUSAGE = ('')
        self.PIZZA_TOPPINGS_PEPPERONI = ('')
        self.PIZZA_TOPPINGS_BACON = ('')
        self.PIZZA_TOPPINGS_HAMBURGER = ('')
        self.PIZZA_TOPPINGS_CANADIANBACON = ('')
        self.PIZZA_TOPPINGS_CHICKEN = ('')
        self.PIZZA_TOPPINGS_ANCHOVY = ('')
        self.PIZZA_TOPPINGS_MUCHROOM = ('')
        self.PIZZA_TOPPINGS_ONION = ('')
        self.PIZZA_TOPPINGS_GREENPEPPER = ('')
        self.PIZZA_TOPPINGS_BLACKOLIVE = ('')
        self.PIZZA_TOPPINGS_TOMATO = ('')
        self.PIZZA_TOPPINGS_PINEAPPLE = ('')
        self.PIZZA_TOPPINGS_JALAPENO = ('')
        self.PIZZA_TOPPINGS_PEPPERONCINI = ('')
        self.PIZZA_TOPPINGS_SHRIMP = ('')
        
        self.PIZZA_SPECIAL_LIGHTCHEESE = ('ctl00_BP_Content_uOrderOptionSets_rptOrderOptionSets_ctl04_cblItems_1141743')
        self.PIZZA_SPECIAL_NOCHEESE = ('ctl00_BP_Content_uOrderOptionSets_rptOrderOptionSets_ctl04_cblItems_1156042')
        self.PIZZA_SPECIAL_WELLDONE = ('ctl00_BP_Content_uOrderOptionSets_rptOrderOptionSets_ctl04_cblItems_1141746')
        self.PIZZA_SPECIAL_HALFBAKED = ('ctl00_BP_Content_uOrderOptionSets_rptOrderOptionSets_ctl04_cblItems_1141745')
        self.PIZZA_SPECIAL_DONOTCUT = ('ctl00_BP_Content_uOrderOptionSets_rptOrderOptionSets_ctl04_cblItems_1146317')
        self.PIZZA_SPECIAL_THICKERCRUST = ('ctl00_BP_Content_uOrderOptionSets_rptOrderOptionSets_ctl04_cblItems_1219271')
        self.PIZZA_SPECIAL_NOSAUCE = ('ctl00_BP_Content_uOrderOptionSets_rptOrderOptionSets_ctl04_cblItems_1156043')
        self.PIZZA_SPECIAL_LIGHTSAUCE = ('ctl00_BP_Content_uOrderOptionSets_rptOrderOptionSets_ctl04_cblItems_1141747')
        self.PIZZA_SPECIAL_EXTRASAUCE = ('ctl00_BP_Content_uOrderOptionSets_rptOrderOptionSets_ctl04_cblItems_1141748')
        
        self.PIZZA_NOTES = ('ctl00_BP_Content_txtComments')
        
        self.PIZZA_SIDE_REDPEPPER = ('ctl00_BP_Content_uOrderOptionSetsUpsell_rptOrderOptionSets_ctl00_cblItems_1153101')
        self.PIZZA_SIDE_PARMESANCHEESE = ('ctl00_BP_Content_uOrderOptionSetsUpsell_rptOrderOptionSets_ctl00_cblItems_1153102')
        self.PIZZA_SIDE_IMOSHOUSEDRESSING = ('ctl00_BP_Content_uOrderOptionSetsUpsell_rptOrderOptionSets_ctl00_cblItems_1193319')
        self.PIZZA_SIDE_SIDERANCHDRESSING = ('ctl00_BP_Content_uOrderOptionSetsUpsell_rptOrderOptionSets_ctl00_cblItems_1193320')
        
        self.PIZZA_BUTTON_NEXT = ('ctl00_BP_Content_ubtnContinue_btnAction')
        
        #Amount of Orders Created
        self.NUMBER_OF_ORDERS = 5  # 5 seconds
        self.TIME_BETWEEN_ORDERS = 1800 #30 mins IN seconds 
        self.SAVE_SCREENSHOT = '[fill in later}'

    
                               
##################################
#         START PROCESS 
##################################
    def run(self):
        #for i in range(self.NUMBER_OF_ORDERS):
            browser = self.browser
            browser.get(self.IMOS_DOMAIN)
        
            # used to transfur from login page to create account page
            self.PageDirect()
            
            #create new account for order.
            self.AccountCreate()
        
            # Check to see if address works
            # ADD TRY NEW ADDRESS CHECKER (IF/ELSE)
            self.AddressChecker()
            
            # shuffles between delivery & pickup
            self.OrderStatus()
            
            #save screen shot of order created before next order.
           # browser.save_screenshot(self.SAVE_SCREENSHOT)
            
        # 30 mins between orders
       # time.sleep(self.TIME_BETWEEN_ORDERS)


##################################
# STEPS
##################################

    # This Directs you past login screen and goes to account creation
    def PageDirect(self):
        browser = self.browser
        #login page
        browser.find_element_by_id(self.LOGIN_ID).click()
        #register account page
        browser.find_element_by_id(self.REGISTER_ID).click()


    # Creates Random Account Info
    def AccountCreate(self):
        browser = self.browser
        # .clear() will allow the input box to be cleared of any saved infomation
        # .click() will click the id inserted
        browser.find_element_by_id(self.EMAIL_ID).clear()
        browser.find_element_by_id(self.EMAIL_ID).send_keys(self.EMAIL)
        browser.find_element_by_id(self.PASSOWRD_ID).clear()
        browser.find_element_by_id(self.PASSWORD_ID).send_keys(self.PASSWORD)  
        browser.find_element_by_id(self.PASSWORDCONFIRM_ID).clear()
        browser.find_element_by_id(self.PASSWORDCONFIRM_ID).send_keys(self.PASSWORDCONFIRM)
        browser.find_element_by_id(self.PASSWORDHINT_ID).clear()
        browser.find_element_by_id(self.PASSWORDHINT_ID).send_keys(self.PASSWORDHINT)
        browser.find_element_by_id(self.FIRSTNAME_ID).clear()
        browser.find_element_by_id(self.FIRSTNAME_ID).send_keys(self.FIRSTNAME)
        browser.find_element_by_id(self.LASTNAME_ID).clear()
        browser.find_element_by_id(self.LASTNAME_ID).send_keys(self.LASTNAME)    
        browser.find_element_by_id(self.ZIPCODE_ID).clear()
        browser.find_element_by_id(self.ZIPCODE_ID).send_keys(self.ZIPCODE)       
         # Checkbox button for age        
        browser.find_element_by_id(self.AGECONFIRM).click() 
        #final Button On Register Side
        browser.find_element_by_id(self.REGISTER_BUTTON).click()                    
    
    # Shuffles between delivery & pickup
    def OrderStatus(self):
        return random.sample([self.DeliveryCreater, self.PickUpCreater], 1) 
    
    def DeliveryCreater(self):
        # FINAL Button On Delivery Setup Screen
        browser.find_element_by_id(self.NEXT_BUTTON).click()
    
    
    # STOP BROWSER
    def StopBrowser(self):
        browser = self.browser
        browser.driver.quit()
        
        
    
        
if __name__ == "__main__":
    unittest.main() 