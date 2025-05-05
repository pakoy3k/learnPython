import cv2
import pyautogui
import numpy as np

method = cv2.TM_SQDIFF_NORMED
image = pyautogui.screenshot()

image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
cv2.imwrite("miescritorio.png", image)
find_i = cv2.imread('findme.png')
find_i.astype(np.uint8)

result = cv2.matchTemplate(find_i, image, method)
mn,_,mnLoc,_ = cv2.minMaxLoc(result)
MPx,MPy = mnLoc
pyautogui.moveTo(MPx,MPy,2)
pyautogui.click()
