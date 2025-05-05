from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
from pynput.keyboard import Key, Controller
keyboard = Controller()

driver = webdriver.Firefox(executable_path ='./geckodriver')
driver.get("http://google.com")
#login apache access
time.sleep(1)
keyboard.type("tramites")
time.sleep(0.3)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
keyboard.type("toto11234")
time.sleep(0.3)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(17)

## algorithm search
elem = driver.find_element_by_id("searchBox")
elem.clear()
elem.send_keys("K90")
elem.send_keys(Keys.RETURN)
time.sleep(1)
sample_chars = 'trmk90iuloes45cand'
sample_list_chars = ["t","d","de","k90","tramite","titulo","creacion","Test","Medida","prueba","lorem","asd"]
for i in range(10):
    lenght = random.randint(3,10)
    search = "".join((random.choice(sample_chars)) for x in range(lenght))
    print(f"Intent : {i} Search: {search}")
    elem = driver.find_element_by_id("searchBox")
    elem.clear()
    elem.send_keys(search)
    elem.send_keys(Keys.RETURN)
    time.sleep(.5)
for i in range(20):
    search = random.choice(sample_list_chars)
    print(f"Intent : {i} Search: {search}")
    elem = driver.find_element_by_id("searchBox")
    elem.clear()
    elem.send_keys(search)
    elem.send_keys(Keys.RETURN)
    time.sleep(.3)

input("Press Enter to continue...")
#assert "No results found." not in driver.page_source" 
driver.close()
