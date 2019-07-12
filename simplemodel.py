import numpy as np

startWords = dict()
counts = dict()

counter = 0
with open('cleaned.csv', 'r') as f:
    for line in f:
        counter += 1
        line = line.lower()
        if len(line) < 2 or len(line.split()) < 1:
            print('skipping', line)
            continue

        firstWord = line.split()[0]
        if firstWord in startWords.keys():
            startWords[firstWord] += 1
        else:
            startWords[firstWord] = 1

        for word in line.split():
            print('word', word)
            if word in counts.keys():
                counts[word] += 1
            else:
                counts[word] = 1

import operator
counts = sorted(counts.items(), key=operator.itemgetter(1))
counts = dict(counts)

print(list(counts.keys())[-5:])
print(list(counts.values())[-5:])
print(len(counts))
print()
numvals = np.sum(np.array(list(counts.values())) >= 50)
inds = np.array(list(counts.keys())[-numvals:])
print(inds)
indsdict = dict()
for n in range(len(inds)):
    indsdict[inds[n]] = n

transitions = np.zeros((numvals, numvals))

import time
init = time.time()
cnt = 0
with open('cleaned.csv', 'r') as f:
    flen = len(f.readlines())

with open('cleaned.csv', 'r') as f:
    for line in f:
        cnt += 1
        print('time left ', (time.time() - init) * (flen / cnt - 1))
        counter += 1
        line = line.lower()
        if len(line) < 2 or len(line.split()) < 1:
            print('skipping', line)
            continue

        prevWord = line.split()[0]
        for word in line.split()[1:]:
            # m = np.where(inds == prevWord)
            # n = np.where(inds == word)
            if prevWord in inds and word in inds:
                m = indsdict[prevWord]
                n = indsdict[word]
                # print(m, n, prevWord, word)
                transitions[m, n] += 1
                prevWord = word

print(np.sum(transitions))
print(np.nonzero(np.sum(transitions, axis=1)))
print(np.nonzero(np.sum(transitions, axis=1))[0].shape)
print(np.random.choice(np.nonzero(np.sum(transitions, axis=1))[0]))
while True:
    sentence = []
    ind = np.random.choice(np.nonzero(np.sum(transitions, axis=1))[0])
    firstWord = inds[ind]
    sentence.append(firstWord)
    for i in range(10):
        try:
            nextWord = np.random.choice(np.nonzero(transitions[ind, :]))
            sentence.append(inds[nextWord])
        except:
            break
    input('sentence ' + ' '.join(sentence))