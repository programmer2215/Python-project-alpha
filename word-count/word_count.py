from matplotlib import pyplot as plt

count = {}
# Enter file name: 'sherlock.txt'
inp = input('enter a file name: ')
if len(inp) < 1:
    inp = 'sherlock.txt'
a = open(inp)
y = list()
x = list()
for line in a:
    w = line.split()
    for word in w:
        if "\"" in word:
            word.strip("\"")
        if "\'" in word:
            word.strip("\'")

        count[word.lower()] = count.get(word.lower(), 0) + 1
print(count)
# for i, j in count.items():
#    print(f'{i} : {j}')
top_10 = sorted([(v, k) for k, v in count.items()], reverse=True)
print('top ten: ')
for i in top_10:
    y.append(i[0])
for i in top_10:
    x.append(i[1])
for i,j in zip(x[:10], y[:10]):
    print(f'{i} : {j}')
plt.bar(x[:20], y[:20])
plt.xlabel('words')
plt.ylabel('frequency')
plt.show()
'''
# to read .txt files off the internet:
import urllib.request, urllib.parse, urllib.error
count = 0
fh = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = {}
for line in fh:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
'''