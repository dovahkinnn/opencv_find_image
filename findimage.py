import cv2
import numpy as np
import pyautogui
import PIL
from time import time, sleep
import pyscreenshot as ImageGrab
 
def click_image(template_filename,button="left", clicks=1, interval=0.25):
    control = control_image(template_filename)
  
    if(control != False):
        w = control[2]
        h = control[3]
        top_left = control
        bottom_right = (top_left[0] + w, top_left[1] + h)
        center =((top_left[0]+bottom_right[0])/2,(top_left[1]+bottom_right[1])/2)
    
        pyautogui.moveTo(center)
        pyautogui.click(center,button=button,clicks=clicks, interval=interval)
        return "clicked"
    else:
        return"bulunamadi"
 
def control_image(template_filename):
    pyautogui.screenshot('images/current_screen.png')
    screen = cv2.imread('images/current_screen.png',cv2.IMREAD_GRAYSCALE)
    template = cv2.imread(template_filename,cv2.IMREAD_GRAYSCALE)
    if template is None:
        print("failed to load template.")
        return False
    w, h = template.shape[::-1]
    method = 'cv2.TM_CCOEFF_NORMED'
    meth = eval(method)
 
    res = cv2.matchTemplate(screen,template,meth)
    threshold = 0.8
    loc = np.where( res >= threshold)
 
    x,y = loc[::-1]
   
    if len(x) > 0 and len(y) > 0:
        return (x[0],y[0],w, h)
    else:
        return False
 
def get_location_image(template_filename):
    control = control_image(template_filename)
    if(control != False):
        return (control[0],control[1])
    else:
        return False
