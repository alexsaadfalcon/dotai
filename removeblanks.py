import time
from langdetect import detect


with open('cleaned.csv') as f:
    lenf = len(f.readlines())

cnt = 0
init = time.time()
with open('cleaned.csv') as f:
    with open('clean_noblanks.csv', 'w') as of:
        for line in f:
            cnt += 1
            print('time left ', (time.time() - init) * (lenf / cnt - 1))
            if len(line) > 1: # and detect(line) == 'en': # language detect takes way too long
                print(line)
                of.write(line)
            else:
                print('omitting', line)