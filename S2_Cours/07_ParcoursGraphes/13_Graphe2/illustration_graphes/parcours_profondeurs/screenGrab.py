import os
from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

service = FirefoxService(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
dossier = os.getcwd()

for i in range(13):
    driver.get(dossier+'\\parcoursProfondeur'+str(i)+'.html')
    sleep(1)
    driver.get_screenshot_as_file("parcoursProfondeur"+str(i)+".png")

driver.quit()
print("end...")