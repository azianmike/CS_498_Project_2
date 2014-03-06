__author__ = 'michaelluo'

import json
from GenreDictionary import artistGenre

openData = open('jay-friends-music.txt')
allData = json.load(openData)['data']

musicOver20 = []

countKanye = 0

for person in allData:
    #print person['name']
    personMusic = person['music'].split(', ')  #, and space
    if len(personMusic) >= 50:
        personMusic = sorted(personMusic)
        musicOver20.append(personMusic)
        for x in personMusic:
            if artistGenre.has_key(x.lower()) is False:
                print x.lower()



print len(musicOver20)
print countKanye