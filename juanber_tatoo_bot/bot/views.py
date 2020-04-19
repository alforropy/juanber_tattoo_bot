from django.shortcuts import render
from selenium import webdriver
from time import sleep
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import requests
# Create your views here.
def open_selenium(user,password):
    url = "https://quotes15.p.rapidapi.com/quotes/random/"
    querystring = {"language_code":"es"}
    headers = {
        'x-rapidapi-host': "quotes15.p.rapidapi.com",
        'x-rapidapi-key': "9944c39d99msh480a9f77b8903dap182836jsnd22ff35704e6"
        }

    driver = webdriver.Firefox()
    driver.get('https://facebook.com')
    emailelement = driver.find_element(By.XPATH, './/*[@id="email"]')
    passelement = driver.find_element(By.XPATH, './/*[@id="pass"]')
    time.sleep(5)
    emailelement.send_keys(user)
    passelement.send_keys(password)
    elem = driver.find_element(By.XPATH, './/*[@id="loginbutton"]')
    elem.click()
    time.sleep(20)
    driver.get('https://m.facebook.com/JuanBer90/posts/3145288532162154')
    time.sleep(5)
    x=0
    while True:
    	try:
    		response = requests.request("GET", url, headers=headers, params=querystring)
    		text = response.json()['content']
    		statuselement = driver.find_element(By.XPATH, ".//*[@id='composerInput']")
    		button = driver.find_element(By.XPATH, '//input[@value="Comment"]')
    		time.sleep(3)
    		statuselement.send_keys(text)
    		print(x, " comentario: ", text)
    		time.sleep(2)
    		x+=1
    		button.click()
    	except Exception as e:
    		print("ocurrio un error, mas detalles: ", e)

def home(req):
    if req.method=='POST':
        open_selenium(req.POST.get('email'), req.POST.get('password'))
    return render(req, 'index.html')
