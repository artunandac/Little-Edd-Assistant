import feedparser 
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import pyautogui
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

from webdriver_manager.chrome import ChromeDriverManager

print("Welcome Sir\nHow can i help you?\n*****Demo*****")

webdriver = ChromeDriverManager.install(ChromeDriver)
while True:
    edterm = input("$ ")
    ter = edterm.lower()
    terlist = ter.split()
    greetings = {'hi','hello','hey'}
    close = {'goodbye','good bye','bye','bb'}
    love = {'i love you','i love u'}
    if ter in greetings:
        print("Hi")
    if ter == 'how are you':
        print("Fine, thanx and you")
    if ter in close:
        print("Goodbye")
        break
    if ter == 'exit' :
        print("Goodbye")
        os.system("cls")
        break
    if ter == 'i love you' :
        print("Me too :)")
    if ter == 'i love u' :
        print("Me too :)")
    if ter == 'thanx' :
        print("Your welcome;)")
    if ter == 'weather':
        def hava():
            parse = feedparser.parse("http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode=EUR|TR|07400|ALANYA|")
            parse = parse["entries"][0]["summary"]
            parse = parse.split()
            print (parse[2], parse[4], parse[5])
            return (hava)
        hava()

    if "youtube" in terlist:
        if terlist[-1] == "a":
            videoname = ter[8:-2]
        else:
            videoname = ter[8:]
        youtube = webdriver.Chrome()
        youtube.get("https://www.youtube.com/results?search_query=" + videoname)
        youtube.find_element_by_xpath('//*[@id="video-title"]').click()
        if terlist[-1] == "a":
            pyautogui.keyDown("alt")
            pyautogui.keyDown("tab")
            pyautogui.keyUp("alt")
            pyautogui.keyUp("tab")
    
    if "google" in terlist:
        if terlist[-1] == "a":
            searchname = ter[7:-2]
        else:
            searchname = ter[7:]
        google = webdriver.Chrome()
        google.get('http://www.google.com')
        search = google.find_element_by_name('q')
        search.send_keys(searchname)
        search.send_keys(Keys.RETURN)
        if terlist[-1] == "a":
            pyautogui.keyDown("alt")
            pyautogui.keyDown("tab")
            pyautogui.keyUp("alt")
            pyautogui.keyUp("tab")  
    def openinstagram():
        print("Opening Instagram")
        instagram = webdriver.Chrome()
        instagram.get("https://www.instagram.com/")
        time.sleep(0.5)
        insusername = instagram.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        insusername.send_keys("EMAIL")
        inspassword = instagram.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        inspassword.send_keys("PASSWORD")
        inspassword.send_keys(Keys.ENTER)
        time.sleep(4)
        instagram.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        time.sleep(4)
        instagram.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
    if "open" and "instagram" in terlist :
        openinstagram()
    def openbionluk():
        bionluk = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        bionluk.get("https://bionluk.com/login")
        time.sleep(0.5)
        bionluk.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div/div[9]/form/input[1]').send_keys("EMAIL")
        bionluk.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div/div[9]/form/input[2]').send_keys("PASSWORD")
        bionluk.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div/div[9]/form/input[2]').send_keys(Keys.ENTER)
    if "open" and "bionluk" in terlist :
        openbionluk()
    if ter == 'open my accounts' or ("open" and "all" and "accounts" in terlist):
        print("Yes, Sir. Please give me a minute...")
        openinstagram()
        time.sleep(3.55)
        openbionluk()
    if ter == "clear" or ter == "cls":
        os.system("cls")
    if ter == "install chromedriver" or ter == "update chromedriver":
        updater = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        updater.get("https://bionluk.com/login")






