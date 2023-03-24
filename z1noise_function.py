import math
import tkinter as tk
import datetime

timer = 0
def pyshader(func, w, h):
    scr = bytearray((0, 0, 0) * w * h)
    for y in range(h):
        for x in range(w):
            p = (w * y + x) * 3
            scr[p:p + 3] = [max(min(int(c * 255), 255), 0)
                            for c in func(x / w, y / h)]
    return bytes('P6\n%d %d\n255\n' % (w, h), 'ascii') + scr


# Ваш код здесь:
def noise(x, y):
    x += 7
    y += 17
    return int((x + y + y*x + x*x + y*y) ** 5) % 100 / 100

def avg1(n1, n2, drb):
    #drb *= drb ** 5
    drb = math.cos((drb-1)*3.14)/2+0.5
    #drb = (2*drb-1)**3/2.0+0.5
    return min(n1, n2) + abs(n1 - n2) * abs((n1 > n2)-drb)

def value_noise(x, y, n):
    nx = int(x * 1000)
    ox = int(nx // n * n)
    x1 = (ox + n // 2) / 1000.0
    x2 = (ox - n // 2) / 1000.0
    ny = int(y * 1000)
    oy = int(ny // n * n)
    y1 = (oy + n // 2) / 1000.0
    y2 = (oy - n // 2) / 1000.0
    t1 = noise(x2, y2)
    t2 = noise(x1, y2)
    b1 = noise(x2, y1)
    b2 = noise(x1, y1)
    t = avg1(t1, t2, (nx % n) * 1.0 / n)
    b = avg1(b1, b2, (nx % n) * 1.0 / n)
    res = avg1(t, b, (ny % n) * 1.0 / n)
    return res

def func(x, y):
    n = (value_noise(x, y, 304) * 16
         + value_noise(x, y, 134) * 8
         + value_noise(x, y, 56) * 4
         + value_noise(x, y, 22) * 2
         + value_noise(x, y, 10) * 1) / 31
    #n = value_noise(x, y, 100)
    #n = noise(x, y)
    #n = datetime.datetime.now().microsecond / 1000000.0
    r = 0.1+math.log(1.0+n)
    g = 0.1+math.log(1.4+n)
    #r = n
    #g = n
    b = 1
    return r, g, b


def update():
    global label
    global img
    img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
    #label.pack()
    label.config(image=img)
    label.after(10, update)
    
    
#timer = datetime.datetime.now().microsecond // 100 % 100
label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
#label.after(10, update)
#tk.mainloop()
