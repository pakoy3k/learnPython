from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path ='./geckodriver')
driver.get("http://bugzilla.ensenada.gob.mx/~tramites/")
time.sleep(2)
for i in range(100):
    print(f'Rdeeffresh {i}')
    driver.refresh()
    time.sleep(1)
driver.close()
