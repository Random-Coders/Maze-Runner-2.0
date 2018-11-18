import numpy as np
from PIL import ImageGrab
import cv2
import time
from matplotlib import pyplot as plt



def screen_record():
    last_time = time.time()
    while(True):
        # 800x600 windowed mode
        #printscreen =  np.array(ImageGrab.grab(bbox=(0,40,800,490)))

        img_rgba = cv2.imread('Resources/testimg.png',cv2.IMREAD_UNCHANGED)
        img_gray = cv2.cvtColor(img_rgba, cv2.COLOR_BGRA2GRAY)
        template = cv2.cvtColor(cv2.imread('Resources/base2.png',cv2.IMREAD_UNCHANGED),cv2.COLOR_BGRA2GRAY)

        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

        threshold = 0.5
        loc = np.where (res >= threshold)

        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_rgba, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

        #cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        cv2.imshow('window2', img_rgba)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


screen_record()
