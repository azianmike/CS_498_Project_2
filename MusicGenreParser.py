__author__ = 'michaelluo'

import json

openData = open('jay-friends-music.txt')
allData = json.load(openData)['data']

musicOver20 = []

countKanye = 0

for person in allData:
    #print person['name']
    personMusic = person['music'].split(',')
    if len(personMusic) >= 50:
        musicOver20.append(personMusic)
        print personMusic
        if 'Kanye West' in personMusic:
            countKanye+=1

print len(musicOver20)
print countKanye