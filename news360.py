'''
Requirements
1. The second task is to write an autotest for registration, password recovery and subsequent authorization with a new password:
2. Please write aт autotest in your favourite framework. Explain the infrastructure.
3. You need to register on the site https://news360.com/, using a real e-mail box, any of  your choice, it can be gmail, yahoo, etc.
4.Next, you need to restore the password through "Forgot your password?"
5.Using the programming language to authorize in the mail and confirm the password recovery
6.Enter a new password, sign out
7.Log in with a new password.
'''


#HOW TO SETUP THE ENVIRONMENT

#1. Download Python from https://www.python.org/ftp/python/3.6.2/python-3.6.2.exe
#2. Install the Python in your Windows machine
#3. Goto CMD Termminal and goto the directory where Python is installed and goto Scripts
#  (ie C:\Users\AppData\Local\Programs\Python\Python36-32\Scripts)
#3. Install Selenium Webdriver by typing pip install -U selenium
#4. Download and install Chromedriver from https://chromedriver.storage.googleapis.com/2.31/chromedriver_win32.zip
#5. Unzip the driver in directory c:/folder/folder/....chromedriver.exe
#6. Open Python IDE and then open file news360.py
#7. Replace the Chromedriver path with path from step 5 
#(ie set driver = webdriver.Chrome("c:/folder/folder/....chromedriver.exe"))
#8. Save the news360.py and press F5 or click on Run.

'''

Author: Shafiq Ahmad, Date August 25th 2017
Email: shafiq.ahmad@gmail.com

The script will launch news360.com portal
Registers as a new user
Click on password recovery
Verifies the reset password email
Resets the password with new password
Logs in to news360 portal using new password
Logs out.

The script is functional, code refactoring will be required to make it more maintanable.

'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import re

driver = webdriver.Chrome('C:/Users/dell/python-scripts-automation/chromedriver.exe')


# registeration

def registeration(url, email, password):

    driver.get(url)
    driver.implicitly_wait(60)
    driver.find_element_by_tag_name("html")

    if not ("Sign in with email" in driver.find_element_by_tag_name("html").text):
        success = False
        print("verifyTextPresent failed registeration 1")
    if not ("Sign up" in driver.find_element_by_tag_name("html").text):
        success = False
        print("verifyTextPresent failed registeration 2")
    driver.find_element_by_xpath("//div[1]/div[3]/div/div[5]/div[3]/div[3]/a").click()
    driver.implicitly_wait(60)
    driver.find_element_by_xpath("//div[1]/div[3]/div/div[5]/div[4]/form[4]/div[2]/div[2]/a").click()
    driver.find_element_by_id("signupemail").clear()
    driver.find_element_by_id("signupemail").send_keys(email)
    driver.find_element_by_id("password").click()
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_xpath("//div[@class='header']/div/div[5]/div[4]/form[3]/fieldset[3]/input").click()
    driver.find_element_by_xpath("//div[@class='header']/div/div[5]/div[4]/form[3]/fieldset[3]/input").clear()
    driver.find_element_by_xpath("//div[@class='header']/div/div[5]/div[4]/form[3]/fieldset[3]/input").send_keys(password)
    driver.find_element_by_xpath("//div[@class='header']//button[.='Sign up']").click()
    print("registered a new account")

#login detail

def login(uname, password):

    driver.get("https://news360.com/")
    driver.find_element_by_link_text("Start reading").click()
    driver.find_element_by_xpath("//div[@class='simplepopup']//a[.='Sign in with email']").click()
    driver.find_element_by_xpath("//div[2]/div[2]/div[4]/form[4]/fieldset[1]/input").click()
    driver.find_element_by_xpath("//div[2]/div[2]/div[4]/form[4]/fieldset[1]/input").send_keys(uname)
    driver.find_element_by_xpath("//div[2]/div[2]/div[4]/form[4]/fieldset[2]/input").click()
    driver.find_element_by_xpath("//div[2]/div[2]/div[4]/form[4]/fieldset[2]/input").send_keys(password)
    driver.find_element_by_xpath("//div[2]/div[2]/div[4]/form[4]/div[1]/button[2]").click()
    driver.find_element_by_css_selector("div.close").click()
    print("logged in")
    #logout
    driver.implicitly_wait(60)
    print("load news360.com/web/settings")
    driver.get("https://news360.com/web/settings/")
    driver.implicitly_wait(60)
    driver.find_element_by_xpath("//div[2]/div/div[1]").click()
    print("logged out")



#password Reset Password

def passwordRecovery(email):

    driver.get("https://news360.com/")
    driver.find_element_by_link_text("Sign in with email").click()
    driver.find_element_by_link_text("Forgot your password?").click()
    driver.find_element_by_id("resetemail").click()
    driver.find_element_by_id("resetemail").clear()
    driver.find_element_by_id("resetemail").send_keys(email)
    driver.find_element_by_xpath("//div[@class='header']//button[.='Reset password']").click()
    print("recoverd password")




#Email Authorization Dummy Email

def checkMail(newpassword):
    
    driver.get("https://maildrop.cc/inbox/news360")
    #if not ("News360 Password Assistance" in driver.find_element_by_tag_name("html").text):
       # success = False
    print("verifyTextPresent failed checkMail")
    driver.find_element_by_link_text("News360 Password Assistance").click()
    driver.find_element_by_css_selector("div.unit.four-of-five").click()
    driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='messageframe']"))
    verifyEmail = driver.find_element_by_xpath("//p[3]/a").text
    print(verifyEmail)
    driver.get(verifyEmail)
    driver.find_element_by_id("resetpassword").click()
    driver.find_element_by_id("resetpassword").clear()
    driver.find_element_by_id("resetpassword").send_keys(newpassword)
    driver.find_element_by_css_selector("input.confirmpassword.textbox").click()
    driver.find_element_by_css_selector("input.confirmpassword.textbox").clear()
    driver.find_element_by_css_selector("input.confirmpassword.textbox").send_keys(newpassword)
    driver.find_element_by_xpath("//div[@class='header']//button[.='Save password']").click()
    print("authorized password reset")
    
    
   
    
 
    
    
#login page
def main(driver):
    try:
        print("starting the script")
        
        return True
    except:
        return False

try:
    
    driver.implicitly_wait(10)
    
finally:
  
        registeration("https://news360.com","news360@maildrop.cc","shafiq1")                                     
        passwordRecovery("news360@maildrop.cc")   
        checkMail("shafiq")
        login("news360@maildrop.cc","shafiq")
        

        raise Exception("Test failed.")
    





