import unittest
from selenium import webdriver
from time import sleep





class Test(unittest.TestCase):
    def testName(self):
        self.driver = webdriver.Chrome(executable_path="E:\python trial\chromedriver_win32\chromedriver.exe")  # chrome driver location 
        self.driver.maximize_window()

        self.driver.get("http://www.gmail.com")   
        
       # self.assertTrue(self.driver.find_element_by_xpath("//*[@id='yDmH0d']/div[1]/div[2]"))
       #//*[@id="headingSubtext"]/span[text()="to continue to Gmail"]
       
       # asserting gmail 
        self.assertTrue(self.driver.find_element_by_xpath("//*[@id='headingSubtext']/span"))
        
        # forgot email
        
        self.driver.find_element_by_xpath("//button[text()='Forgot email?']").click()
        
        
        #TC:6 navigation check ---
        
        # not working when i add text after span 
        
        self.assertTrue(self.driver.find_element_by_xpath("//span[text()='Enter your phone number or recovery email']"))
        
      
      
        # creating account 
    
        self.driver.find_element_by_xpath("//span[text()='Create account']").click()
        
        self.driver.find_element_by_xpath("//div[text()='For myself']").click()
        
        # TC:5 checking if navigated to create account page  
        
        self.assertTrue(self.driver.find_element_by_xpath("//h1[text()='Create your Google Account']"))
        # currently working//*[@id="headingSubtext"]/span
        
        
        self.driver.find_element_by_xpath("//*[@id='identifierNext']/span/span").click()
        
        # TC:1 asserting enter phone or
        
        self.assertTrue(self.driver.find_element_by_xpath("//div[text()='Enter an email or phone number']"))
        
    #    elem = self.driver.find_element_by_xpath("//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/span/section/div/span/div[1]/div/div[2]/div[2]/div")
        
        
        self.driver.find_element_by_name("identifier").send_keys("projectt432@gmail.com")

        self.driver.find_element_by_xpath("//*[@id='identifierNext']/span/span").click()    # next xpath
        
        # TC:2 to check if email id is correct
        
        self.assertTrue(self.driver.find_element_by_xpath("//span[text()='Welcome']"))
        
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_name("password").send_keys("projecttesting")



        self.driver.find_element_by_xpath("//*[@id='passwordNext']/span/span").click()           # next xpath
        self.driver.implicitly_wait(15)
        
        #TC:3 check for successful login -- inbox 
        
        self.assertTrue(self.driver.find_element_by_xpath("//a[text()='Inbox']"))
        
        
        #TC:7 Theme change
        
        # how to pick uniquely and randomly 
        
        self.driver.find_element_by_xpath("//div[@aria-label='Settings']").click()
        
        self.driver.find_element_by_xpath("//div[text()='Themes']").click()
       
        # //div[@aria-label="By: Grzegorz Głowaty"] by aria-label also 
        self.driver.find_element_by_xpath("//div[@bgid='custom-5']").click()
        
        
        
        
        
        
        
        
        # sign out 
        
        self.driver.implicitly_wait(15)


        self.driver.find_element_by_xpath("//*[@id='gb']/div[2]/div[3]/div/div[2]/div/a/span").click()

        self.driver.implicitly_wait(10)

        self.driver.find_element_by_xpath("//*[@id='gb_71']").click()
        
        # TC: 4 check for successful logout -choose another account
        self.assertTrue(self.driver.find_element_by_xpath("//div[@class='jXeDnc']//h1//span"))
        


        


        
     #   self.driver.find_element_by_xpath("//*[@id='identifierNext']/span/span").click()
        
     #   self.driver.implicitly_wait(5)

    
        # self.assertEqual(self.driver.find_element_by_xpath("//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/span/section/div/span/div[1]/div/div[2]/div[2]/div","Enter an email or phone number"))

    #    self.driver.implicitly_wait(5)


        """

        self.driver.find_element_by_name("identifier").send_keys("projectt432@gmail.com")

        self.driver.find_element_by_xpath("//*[@id='identifierNext']/span/span").click()    # next xpath
        
        #actual_error = self.driver.find_element_by_xpath("//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/span/section/div/span/div[1]/div/div[2]/div[2]/div").getText()

        #self.expected_error = "Enter an email or phone number"
        
        
        #self.assertEqual(actual_error,"True")
        
        
        self.driver.implicitly_wait(5)
        
        self.driver.find_element_by_name("password").send_keys("projecttesting")



        self.driver.find_element_by_xpath("//*[@id='passwordNext']/span/span").click()           # next xpath
        self.driver.implicitly_wait(15)

        
    
        # click on compose button 
        
        self.driver.find_element_by_css_selector(".aic .z0 div").click()
        
        #TC:7 check for to cc bcc
        
        self.assertTrue(self.driver.find_element_by_xpath("//div[@class='fX aXjCH']"))
        
        # Recipient
        
        self.driver.find_element_by_css_selector(".oj div textarea").send_keys("projectt432@gmail.com")
        
        # subject
        
        self.assertEqual(self.driver.find_element_by_xpath("//div[@class='aoD az6']"))
        
        self.driver.find_element_by_css_selector(".aoD.az6 input").send_keys("Testing successful")
        
        # body message
        
        self.driver.find_element_by_css_selector(".Ar.Au div").send_keys("Hello Sushmitha")
        
        
        
        # attachment
        
        self.driver.implicitly_wait(5)
        
    
        
        self.driver.find_element_by_xpath("//*[@id=':bj']").click()
        
        self.driver.implicitly_wait(10)
        
        #self.driver.find_element_by_xpath("C:\\Users\\sunny\\Downloads\\word1.png").click()
        
      
        
        self.driver.implicitly_wait(5)
        
       #self.driver.find_element_by_css_selector(".wG.J-Z-I").send_keys("C:\\Users\\sunny\\Downloads\\me wid prof.JPG")
        
        # send button
    
        self.driver.find_element_by_css_selector(".T-I.J-J5-Ji.aoO.v7.T-I-atl.L3").click()
        
        self.driver.find_element_by_css_selector("tr.btC td:nth-of-type(1) div div:nth-of-type(2)").click()
        """
        
        
        
        
        
        
        
"""        

        self.driver.find_element_by_name("password").send_keys("projecttesting")



        self.driver.find_element_by_xpath("//*[@id='passwordNext']/span/span").click()           # next xpath
        self.driver.implicitly_wait(15)


        self.driver.find_element_by_xpath("//*[@id='gb']/div[2]/div[3]/div/div[2]/div/a/span").click()




        self.driver.implicitly_wait(10)

        self.driver.find_element_by_xpath("//*[@id='gb_71']").click()
        
       
"""

if __name__ == "__main__":
    unittest.main()
    
    
    
"""   ##### with out class #######




driver = webdriver.Chrome(executable_path="E:\python trial\chromedriver_win32\chromedriver.exe")  # chrome driver location 
driver.maximize_window()

driver.get("http://www.gmail.com")   



driver.find_element_by_name("identifier").send_keys("projectt432@gmail.com")

driver.find_element_by_xpath("//*[@id='identifierNext']/span/span").click()    # next xpath


# error path


actual_error = driver.find_element_by_xpath("//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/span/section/div/span/div[1]/div/div[2]/div[2]/div").getText()

expected_error = "Enter an email or phone number"
       
      
#password

driver.implicitly_wait(5)

driver.find_element_by_name("password").send_keys("projecttesting")



driver.find_element_by_xpath("//*[@id='passwordNext']/span/span").click()           # next xpath


# sign out 

driver.implicitly_wait(15)


driver.find_element_by_xpath("//*[@id='gb']/div[2]/div[3]/div/div[2]/div/a/span").click()

driver.implicitly_wait(10)

driver.find_element_by_xpath("//*[@id='gb_71']").click()
"""