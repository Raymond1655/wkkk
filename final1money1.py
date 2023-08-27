import  time
import typing
from  PyQt5.QtCore import QObject, QThread,pyqtSignal
import pydirectinput

import pyautogui
import win32con
import win32gui
import random
from PIL import ImageGrab
import ddddocr


class money1(QThread):
    money1num1=pyqtSignal(str)

    def __init__(self,t,y,u,parent=None):
        super(money1,self).__init__(parent)
        self.t=t
        self.y=y
        self.u=u
    
    def run(self):
        ll1=0
        time.sleep(2)
        start1=[0,0]
        start1a=[0,0]
        while True:

            while True:
                part=pyautogui.locateOnScreen('picture/money/1.png',confidence=0.9)
                if part is None:
                    break
                if part is not None:
                    start1[0]=part[0]
                    start1[1]=part[1]
                    break
            if part is None:
                break



            #在自由
            while True:
                parta=pyautogui.locateOnScreen('picture/money/2.png',confidence=0.9)
                if parta is not None:
                    break
            
            #存倉
            if ll1>50:
                while True:
                    parta=pyautogui.locateOnScreen('picture/money/18.png',region=(start1[0]+1013,start1[1]-480,321,264),confidence=0.9)
                    if parta is not None:
                        time.sleep(2)
                        pydirectinput.moveTo(parta[0],parta[1])
                        pydirectinput.doubleClick()
                        time.sleep(2)
                        pydirectinput.press('1')
                        time.sleep(0.5)
                        pydirectinput.press('2')
                        time.sleep(0.5)
                        pydirectinput.press('3')
                        time.sleep(0.5)
                        pydirectinput.press('4')
                        time.sleep(0.5)
                        pydirectinput.press('5')
                        time.sleep(0.5)
                        pydirectinput.press('6')
                        time.sleep(1)
                        pydirectinput.press('enter')
                        break

                

                while True:
                    print(0000)
                    partd=pyautogui.locateOnScreen('picture/money/23.png',region=(start1[0]+591,start1[1]-330,338,154),confidence=0.9)
                    if partd is not None:
                        print(1111)
                        break

                    if partd is None:
                        while True:
                            print(2222)
                            parta=pyautogui.locateOnScreen('picture/money/21.png',region=(start1[0]+591,start1[1]-330,338,154),confidence=0.9)
                            if parta is not None:
                                time.sleep(2)
                                pydirectinput.moveTo(parta[0],parta[1])
                                pydirectinput.click()
                                break

                        while True:
                            print(3333)
                            parta=pyautogui.locateOnScreen('picture/money/22.png',confidence=0.9)
                            if parta is not None:
                                time.sleep(2)
                                pydirectinput.moveTo(parta[0],parta[1])
                                pydirectinput.click()
                                break
                        break
                
                while True:
                    print(4444)
                    parta=pyautogui.locateOnScreen('picture/money/24.png',confidence=0.9)
                    if parta is not None:
                        time.sleep(2)
                        pydirectinput.moveTo(parta[0],parta[1])
                        pydirectinput.click()
                        break







            ll1=0
            #點楓之谷世界
            print(41111)
            while True:
                parta=pyautogui.locateOnScreen('picture/money/3.png',confidence=0.9)
                partd=pyautogui.locateOnScreen('picture/money/4.png',confidence=0.9)
                if partd is not None:
                    break
                if parta is not None:
                    print(5111)
                    time.sleep(2)
                    pydirectinput.moveTo(parta[0],parta[1])
                    pydirectinput.doubleClick()
                    time.sleep(1)
                    pydirectinput.moveTo(parta[0]+150,parta[1])

                    
                
                


            #點地圖傳送
            while True:
                parta=pyautogui.locateOnScreen('picture/money/4.png',confidence=0.9)
                if parta is not None:
                    time.sleep(2)
                    pydirectinput.moveTo(parta[0],parta[1])
                    pydirectinput.click()
                    break

            #點打幣
            while True:
                parta=pyautogui.locateOnScreen('picture/money/5.png',confidence=0.9)
                if parta is not None:
                    time.sleep(2)
                    pydirectinput.moveTo(parta[0],parta[1])
                    pydirectinput.click()
                    break

            #點是
            while True:
                parta=pyautogui.locateOnScreen('picture/money/6.png',confidence=0.9)
                if parta is not None:
                    time.sleep(2)
                    pydirectinput.moveTo(parta[0],parta[1])
                    pydirectinput.click()
                    break

            
            #判斷到場
            while True:
                parta=pyautogui.locateOnScreen('picture/money/8.png',confidence=0.9)
                if parta is not None:
                    break
            
            
            #判斷正確圖
            kk1=0
            while True:
                parta=pyautogui.locateOnScreen('picture/money/13.png',confidence=0.9)
                if parta is not None:
                    break
                if parta is None:
                    partd=pyautogui.locateOnScreen('picture/money/16.png',confidence=0.9)
                    if partd is not None:
                        time.sleep(1)
                        pydirectinput.moveTo(partd[0],partd[1])
                        time.sleep(0.5)
                        pydirectinput.doubleClick()
                        time.sleep(1)
                        pydirectinput.press('right')
                        time.sleep(0.5)
                        pydirectinput.press('enter')
                        break
                    kk1=kk1+1
                    time.sleep(1)    
                    if kk1>15:
                        break
            

            if parta is not None:      
                #點NPC
                gg=0
                while True:
                    parta=pyautogui.locateOnScreen('picture/money/7.png',confidence=0.9)
                    if parta is not None:
                        time.sleep(1)
                        pydirectinput.moveTo(parta[0],parta[1])
                        pydirectinput.doubleClick()
                        break
                    time.sleep(1)
                    gg=gg+1
                    if gg>16:
                        break
                    



                if gg<15:


                    #確認點到
                    while True:
                        parta=pyautogui.locateOnScreen('picture/money/9.png',confidence=0.9)
                        if parta is not None:
                            time.sleep(1)
                            break



                    #截圖
                    while True:
                        parta=pyautogui.locateOnScreen('picture/money/1.png',confidence=0.9)
                        if parta is not None:
                            start1a[0]=parta[0]
                            start1a[1]=parta[1]
                            screenshot = ImageGrab.grab((start1[0]+561,start1[1]-441,start1[0]+800,start1[1]-370))
                            screenshot.save('picture/money/screenshot.png')
                            break

                    #判圖
                    i=0
                    ocr=ddddocr.DdddOcr()
                    with open('picture/money/screenshot.png','rb') as f:
                        img_bytes=f.read()
                    res=ocr.classification(img_bytes)


                    #000000000000000000000000000000000000000000000000000000
                    while i < len(res):
                        print(res[i])

                        if res[i] in {"0","零","o","O","Q"}:
                            pydirectinput.press('0')

                        if res[i] in {"1","一","壹","z","t"}:
                            pydirectinput.press('1')

                        if res[i] in {"2","二","貳"}:
                            pydirectinput.press('2')

                        if res[i] in {"3","三","參"}:
                            pydirectinput.press('3')

                        if res[i] in {"4","四","肆"}:
                            pydirectinput.press('4')

                        if res[i] in {"5","五","伍"}:
                            pydirectinput.press('5')

                        if res[i] in {"6","六","陛","陸","白","b"}:
                            pydirectinput.press('6')

                        if res[i] in {"7","七","柒"}:
                            pydirectinput.press('7')

                        if res[i] in {"8","八","捌"}:
                            pydirectinput.press('8')

                        if res[i] in {"9","九","玖","g"}:
                            pydirectinput.press('9')

                        i=i+1

                    #000000000000000000000000000000000000000000000000000000
                    time.sleep(1.5)
                    pydirectinput.press('enter')
                    time.sleep(2)

                #驗證成功或自由
                ll1=0
                while True:
                    partb=pyautogui.locateOnScreen('picture/money/2.png',confidence=0.9)
                    if partb is not None:
                        break
                    parta=pyautogui.locateOnScreen('picture/money/10.png',confidence=0.9)
                    if parta is not None:
                        #判斷在場內
                        while True:
                            parta=pyautogui.locateOnScreen('picture/money/11.png',confidence=0.9)
                            if parta is not None:
                                time.sleep(1)
                                pydirectinput.moveTo(parta[0],parta[1])
                                pydirectinput.doubleClick()
                                break
                        break
                    partc=pyautogui.locateOnScreen('picture/money/8.png',confidence=0.9)
                    if partc is not None:
                        break
                    
                if partb is None:  
                    #判斷場景
                    while True:
                        parta=pyautogui.locateOnScreen('picture/money/8.png',confidence=0.9)
                        if parta is not None:
                            start1a[0]=parta[0]
                            start1a[1]=parta[1]
                            print(start1a[0],start1a[1])
                            break
                    pydirectinput.keyDown('left')
                    time.sleep(5)
                    pydirectinput.keyUp('left')
                    print(self.t)
                    if self.t==10:
                        print('兩倍')
                        parta=pyautogui.locateOnScreen('picture/money/14.png',confidence=0.9)
                        if parta is None:
                            partd=pyautogui.locateOnScreen('picture/money/15.png',confidence=0.9)
                            if partd is None:
                                print('兩倍有')
                                pydirectinput.press('u')

                    if self.t==20:
                        print('三倍')
                        parta=pyautogui.locateOnScreen('picture/money/14.png',confidence=0.9)
                        if parta is None:
                            partd=pyautogui.locateOnScreen('picture/money/15.png',confidence=0.9)
                            if partd is None:
                                print('三倍有')
                                pydirectinput.press('y')




                    #打
                    hh1=0
                    hh2=0
                    while True:
                        gg1=pyautogui.locateOnScreen('picture/money/12.png',region=(start1a[0]+97,start1a[1]+85,69,29),confidence=0.9)
                        gg2=pyautogui.locateOnScreen('picture/money/12.png',region=(start1a[0]+27,start1a[1]+85,70,29),confidence=0.9)
                        partb=pyautogui.locateOnScreen('picture/money/8.png',confidence=0.9)
                        if partb is None:
                            time.sleep(10)
                            break
                        if gg2 is not None:
                            print('right')
                            pydirectinput.keyDown('right')
                            time.sleep(0.2)
                            pydirectinput.keyUp('right')
                            time.sleep(0.1)
                        if gg1 is not None:
                            print('left')
                            pydirectinput.keyDown('left')
                            time.sleep(0.2)
                            pydirectinput.keyUp('left')
                            time.sleep(0.1)

                        pydirectinput.press('space')
                        time.sleep(0.1)
                        hh1=hh1+1
                        hh2=hh2+1
                        ll1=ll1+1
                        if hh1==1:
                            time.sleep(0.5)
                            pydirectinput.press('a')
                            time.sleep(0.5)
                            pydirectinput.press('d')
                            time.sleep(0.5)
                            pydirectinput.press('e')
                            time.sleep(0.5)
                            pydirectinput.press('w')
                            time.sleep(0.5)
                            pydirectinput.press('q')
                            time.sleep(0.5)

                        if hh1==250:
                            time.sleep(0.5)
                            pydirectinput.press('d')
                            time.sleep(0.5)
                            pydirectinput.press('e')
                            time.sleep(0.5)
                            pydirectinput.press('w')
                            time.sleep(0.5)
                            pydirectinput.press('q')
                            time.sleep(0.5)
                            pydirectinput.press('s')
                            time.sleep(0.5)
                            hh1=5

                        if hh2==30:
                            time.sleep(0.5)
                            pydirectinput.press('a')
                            time.sleep(0.5)
                            pydirectinput.press('right')
                            time.sleep(0.5)
                            hh2=0
        