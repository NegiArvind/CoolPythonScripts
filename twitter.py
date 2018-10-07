
# This script is used to login twiiter account and then tweet the message using selenium webdriver

from selenium import webdriver
from getpass import getpass
from time import sleep

username=input("Enter your username or email :")
password=input("Enter your password : ")
message=input("Enter the tweet message : ")

driver=webdriver.Firefox()
driver.get("https://twitter.com/login") # open the website

usr_box=driver.find_element_by_class_name("js-username-field") # find specific element in website  page
usr_box.send_keys(username) # send username to username placeholder in website
sleep(3) # sleep for 3 second

password_box=driver.find_element_by_class_name("js-password-field") # find specific element in webstie page
password_box.send_keys(password) # send password to password placeholder in website
sleep(3)

submit_button=driver.find_element_by_css_selector("button.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium")
submit_button.submit() # submitting the detail via submit button
sleep(20)

tweet_box=driver.find_element_by_id("tweet-box-home-timeline")
tweet_box.send_keys(message)
sleep(20)

tweet_button=driver.find_element_by_css_selector("button.tweet-action.EdgeButton.EdgeButton--primary.js-tweet-btn")
print("button pressed\n")
tweet_button.submit()
