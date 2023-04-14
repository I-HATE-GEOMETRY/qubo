from PIL.ImageGrab import grab
from numpy import array
import time
import PIL
import pyautogui

def main():
    time.sleep(3)

    t = time.time()

    y0 = 0

    for a in range(1000):
        mas = array(grab(bbox = (130, 120, 220, 300)))

        y = 0
        count = 0

        for i in range(0, len(mas), 2):
            for j in range(0, len(mas[i]), 2):
                if mas[i][j][0] >= 220:
                    count += 1
                    y += j
                    #mas[i][j][1] = 0
                    #mas[i][j][0] = 0
        if count == 0:
            print('count = 0')
            break
        y /= count

        v = (y - y0) / (time.time() - t)

        print(v, end = ' ')
        
        if v >= 13 and v <= 20:
            print('click', end = '')
            pyautogui.mouseDown()
            time.sleep(1.05)
        print()
        t = time.time()
        y0 = y
        #print(len(mas >= 255), count)
        #print(y)
        #time.sleep(0.1)
        #break

    print(time.time() - t)

    img = PIL.Image.fromarray(mas)

    img.save('qubo.png')


    #print(mas[0][0])

main()
