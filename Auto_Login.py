#auto facebook login.
from tkinter import *  #GUI
from selenium import webdriver #Firefox

def login():
    browser=webdriver.Firefox()
    browser.get("https://facebook.com")
    login=browser.find_element_by_id("email")
    passw=browser.find_element_by_id("pass")
    login.send_keys("") #enter email in ""
    passw.send_keys("")   #enter password in ""
    browser.find_element_by_id("u_0_n").click()

root = Tk()
root.title("Facebook Login")
root.geometry("200x100")
app=Frame(root)
app.grid()
but=Button(text="login",command=login)
but.grid()
root.mainloop()
