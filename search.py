from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
from pynput.keyboard import Key, Controller
keyboard = Controller()

driver = webdriver.Firefox(executable_path ='./geckodriver')
driver.get("http://bugzilla.ensenada.gob.mx/~tramites")
#assert "Tramites Ensenada" in driver.title

#login apache access
time.sleep(1)
keyboard.type("innovacion")
time.sleep(0.3)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
keyboard.type("pakoereselmejor")
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
#driver.get("http://bugzilla.ensenada.gob.mx/~tramites/login")
for i in range(100):
	lenght = random.randint(3,10)
	search = "".join((random.choice(sample_chars)) for x in range(lenght))
	print(f"Intent : {i} Search: {search}")
	elem = driver.find_element_by_id("searchBox")
	elem.clear()
	elem.send_keys(search)
	elem.send_keys(Keys.RETURN)
	time.sleep(.1)
for i in range(2000):
	search = random.choice(sample_list_chars)
	print(f"Intent : {i} Search: {search}")
	elem = driver.find_element_by_id("searchBox")
	elem.clear()
	elem.send_keys(search)
	elem.send_keys(Keys.RETURN)
	time.sleep(.2)

input("Press Enter to continue...")
#assert "No results found." not in driver.page_source" 
driver.close()
