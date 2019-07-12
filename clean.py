import pandas as pd
import os
from langdetect import detect
import string

if os.path.exists('train.csv'):
    chats = pd.read_csv('train.csv')
else:
    chats = pd.read_csv('dota2_chat_messages.csv')['text']
    train = .1
    train = round(train*len(chats))
    # with open('train.csv', 'w') as of:
    #     of.write('chats\n')
    #     for line in chats[:train]:
    #         of.write(line + u'\n')

print(detect('tu eres tonto'))
print(detect('testing random text'))
print(detect(chats[0]))


# input(chats[-10:])
wordcounts = dict()
# chats = []
# with open('dota2_chat_messages.csv', 'r') as f:
#     for line in f:
#         line = line.strip()
#         line = line.decode('utf-8','ignore').encode("utf-8")

missedcount = 0
import time
init = time.time()
n = 0
def convert(line):
    line = line.translate(str.maketrans('', '', string.punctuation))
    return line.encode('ascii', 'replace').decode('utf-8')


with open('cleaned.csv', 'w') as of:
    for line in chats:
        line = str(line)
        n += 1
        print('DONE WITH ', n / len(chats))
        print('time left ', (time.time() - init) * (len(chats) / (n + 1) - 1))
        l = convert(line)
        if '?' not in l:
            print('old', line, '\nnew', l)
            of.write(l + '\n')
        # try:
        #     pass
        # except Exception as e:
        #     print(type(e), e)
        #     missedcount += 1

print('MISSED ', missedcount)

    # for word in line.split():
    #     try:
    #         wordcounts[word] += 1
    #     except:
    #         wordcounts[word] = 1

print(wordcounts)