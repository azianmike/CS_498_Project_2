__author__ = 'michaelluo'

import json
from GenreDictionary import artistGenre

openData = open('jay-friends-music.txt')
allData = json.load(openData)['data']

musicOver50 = []
musicOver50List = []

#Getting data from txt file and putting into one giant list
for person in allData:
    #print person['name']
    personMusic = person['music'].split(', ')  #, and space
    if len(personMusic) >= 50:
        personMusic = sorted(personMusic)
        musicOver50 = musicOver50 + personMusic
        musicOver50List.append(personMusic)
        # for x in personMusic:
        #     if artistGenre.has_key(x.lower()) is False:
        #         print x.lower()


#classifying artists based on genre
jayBensal={
    'Hip Hop':'0',
    'Rock':'0',
    'Pop':'0',
    'Electronic':'0',
    'Alternative':'0',
    'Country':'0',
    'Other':'0',
    'Not classified':'0'
}
for artist in musicOver50:
    if artistGenre.has_key(artist.lower()):
        genre = artistGenre[artist.lower()]
        count = int(jayBensal[genre])+1
        jayBensal[genre] = count
    else:
        count = int(jayBensal['Not classified']) + 1
        jayBensal['Not classified'] = count

count = int(jayBensal['Other'])
jayBensal['Other'] = '0'
notCount = int(jayBensal['Not classified'])
jayBensal['Not classified'] = count+notCount
#print jayBensal

#classifying each person
print musicOver50List
personLikesList = []
#goes through every person
for person in musicOver50List:
    personLikes = {
        'Hip Hop':'0',
        'Rock':'0',
        'Pop':'0',
        'Electronic':'0',
        'Alternative':'0',
        'Country':'0',
        'Other':'0',
        'Not classified':'0'
    }
    #goes through every artist in persons like
    for artist in person:
        if artistGenre.has_key(artist.lower()):
            genre = artistGenre[artist.lower()]
            count = int(personLikes[genre])+1
            personLikes[genre] = count
        else:
            count = int(personLikes['Not classified']) + 1
            personLikes['Not classified'] = count

    personLikesList.append(personLikes)

#prints out
for x in personLikesList:
    print x
