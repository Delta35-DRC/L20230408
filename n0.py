from random import randint
import time
txt = []
while True:
    time.sleep(0.1)
    for i in range(randint(5, 30)):
        txt.append(randint(0, 1))
    print(txt)
    txt = []
