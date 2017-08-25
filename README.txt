'''
Requirements
1. The second task is to write an autotest for registration, password recovery and subsequent authorization with a new password:
2. Please write a? autotest in your favourite framework. Explain the infrastructure.
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