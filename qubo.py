import pyscreenshot
import time
import numpy
import PIL

def main():
    time.sleep(3)

    t = time.time()

    for a in range(100):
        mas = numpy.array(pyscreenshot.grab(bbox = (130, 120, 220, 300)))

        y = 0
        count = 0

        for i in range(0, len(mas), 6):
            for j in range(0, len(mas[i]), 6):
                if mas[i][j][0] >= 220:
                    count += 1
                    y += j
                    #mas[i][j][1] = 0
                    #mas[i][j][0] = 0
        if count == 0:
            print('count = 0')
            break
        y /= count
        #print(len(mas >= 255), count)
        #print(y)
        #time.sleep(0.1)
        #break

    print(time.time() - t)

    img = PIL.Image.fromarray(mas)

    img.save('qubo.png')


    #print(mas[0][0])

main()
