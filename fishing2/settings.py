import pyautogui
from keyscodes import *
import win32api, win32con, win32gui, win32com.client
import time, win32com.client
from PIL import Image
import time
from directkeys import PressKey, ReleaseKey

#Ставим задержку перед запуском
print(" ")
print("Привет!!! Это бета версия Fishing бота для Астериоса. Сейчас запустится программа")
print(" ")

delay = 5
m = 0
while m < delay:
    delayRusilt = delay - m
    print("до запуска осталось: ", delayRusilt, "секунд")
    time.sleep(1)
    m += 1


def delayNew(delayCount, text):
    delay = delayCount
    m = 0
    while m < delay:
        delayRusilt = delay - m
        print(text, delayRusilt, "секунд")
        time.sleep(1)
        m += 1
text1 = "Для получения координат осталось: "

print(" ")
print("Забросьте удочку")
text2 = "до следующего действия осталось: "
delayNew(5, text2)

#верхний левый угол
LEFTcurrentMouseX = 0
LEFTcurrentMouseY = 27
print(" ")
print("Наведите правый нижний угол рамки рыбалки")
delayNew(10, text1)
RIGHTcurrentMouseX, RIGHTcurrentMouseY = pyautogui.position()
print('Отлично, координаты скилы получены. Теперь бот начинает ловить рыбу')
print(" ")


BluePixel =  [(138,197,207), (145,182,188), (73,143,175), (65,143,175), (75,136,165), (67,163,198), (64,129,164), (233,245,223), (185, 220, 214),(16, 122, 163), (66, 130, 162),(90, 174, 201), (56, 156, 196), (83, 187, 221),(46, 108, 152)]

action = 0
LastBlue = 0
i = 0
while i < 1:
    #cкрин определяет нужно ли закидывать удочку
    screenFirst = pyautogui.screenshot('screenshot.png', region=(LEFTcurrentMouseX,LEFTcurrentMouseY, RIGHTcurrentMouseX, RIGHTcurrentMouseY))
    #screenFirst.save(r"C:\Users\Alexc\Documents\fishing\screenshot.png")
    Grey = 0
    for pixel in screenFirst.getdata():
        if pixel == (36, 30, 21):
            Grey += 1
    if Grey < 100:


        #таргет
        key = randomFirstPanel(4)
        PressKey(key)
        ReleaseKey(key)
        time.sleep(1)

        #атаака. Потом написать проверку на взят моб в таргет или нет
        key = randomFirstPanel(5)
        PressKey(key)
        ReleaseKey(key)
        time.sleep(3)


        #Закидываем удочку
        print(" ")
        print("Бот забрасывает удочку", time.ctime())
        key = randomFirstPanel(3)
        PressKey(key)
        ReleaseKey(key)
        time.sleep(4)
    else:  
        while Grey > 100:
            Blue0 = 0
            Grey1 = 0
            BlueExit = 0
            LastGrey = 0
            while BlueExit < 1:
                screenFirst = pyautogui.screenshot('screenshot.png', region=(LEFTcurrentMouseX,LEFTcurrentMouseY, RIGHTcurrentMouseX, RIGHTcurrentMouseY))
                for pixel in screenFirst.getdata():
                    if pixel in BluePixel:
                        Blue0 += 1
                    if pixel == (36, 30, 21):
                        Grey1 += 1  
                if (Blue0 != 0):
                    BlueExit = 1
                elif (Blue0 == 0 and Grey1 < 100):
                    BlueExit = 1
                elif (Blue0 == 0 and Grey1 > 100):
                    Grey1 = 0





            time.sleep(0.25)
            #cделали второй скрин
            screenSecond = pyautogui.screenshot('screenshot2.png', region=(LEFTcurrentMouseX,LEFTcurrentMouseY, RIGHTcurrentMouseX, RIGHTcurrentMouseY))

            Blue1 = 0
            Grey2 = 0
            for pixel in screenSecond.getdata():
                if pixel in BluePixel:
                    Blue1 += 1
                if pixel == (36, 30, 21):
                    Grey2 += 1
           

            time.sleep(0.25)
            #cделали третий скрин
            screenThird = pyautogui.screenshot('screenshot3.png', region=(LEFTcurrentMouseX,LEFTcurrentMouseY, RIGHTcurrentMouseX, RIGHTcurrentMouseY))
            Blue2 = 0
            for pixel in screenThird.getdata():
                if pixel in BluePixel:
                    Blue2 += 1
           

            blueSkrean = [Blue0, Blue1, Blue2]
            Grey = Grey2
               
            n = 0
            nullik = 0
            #считаем количество нулевых пикселей
            while n < 3:
                if (blueSkrean[n] == 0):
                    nullik += 1
                n += 1

            if nullik in [0,1,2]: #Если больше двух скринов с пикселями - то перескрин
                if Grey2 < 100:
                    time.sleep(4)
                    Grey = 0 
                else:
                    s = 0
                    BlueMassivLen = len(blueSkrean) #3
                    firstItem = 0
                    LastItem = 0
                    ListItemID = BlueMassivLen - 1

                    #ищем первый элемент
                    while s < BlueMassivLen:
                        if (blueSkrean[s] != 0):
                            firstItem = s
                            s = BlueMassivLen
                        else: 
                            s += 1

                    #ищем последний элемент
                    while ListItemID < BlueMassivLen:
                        if (blueSkrean[ListItemID] != 0):
                            LastItem = ListItemID
                            ListItemID = BlueMassivLen
                        else: 
                            ListItemID = ListItemID - 1
                    #print("Первый итем Blue",firstItem, " значение - ", blueSkrean[firstItem], " Последний итем Blue",LastItem, " значение - ", blueSkrean[LastItem])
                    #сравнение
                    if (blueSkrean[LastItem] == blueSkrean[firstItem]):
                        if Blue0 == 0:
                            screenFirst.save(r"C:\Users\Alexc\Documents\fishing\perescreean\screenshot.png")
                        if Blue1 == 0:
                            screenSecond.save(r"C:\Users\Alexc\Documents\fishing\perescreean\screenshot2.png")
                        print("Pumping") 
                        key = randomFirstPanel(2)
                        PressKey(key)
                        LastItemName = LastItem + 1
                        ReleaseKey(key)

                       
                        
                        time.sleep(1)
                    
                    if (blueSkrean[LastItem] > blueSkrean[firstItem]):
                        if Blue0 == 0:
                            screenFirst.save(r"C:\Users\Alexc\Documents\fishing\perescreean\screenshot.png")
                        if Blue1 == 0:
                            screenSecond.save(r"C:\Users\Alexc\Documents\fishing\perescreean\screenshot2.png")
                        print("Reeling")
                        key = randomFirstPanel(1)
                        PressKey(key)
                        ReleaseKey(key)    
                        time.sleep(1)  
                        
                  
                    
                     
        

        