__author__ = 'michaelluo'

import json
from GenreDictionary import artistGenre

openData = open('jay-friends-music.txt')
allData = json.load(openData)['data']

musicOver50 = []
musicOver50List = {}

#Getting data from txt file and putting into one giant list
for person in allData:
    #print person['name']
    personMusic = person['music'].split(', ')  #, and space
    if len(personMusic) >= 50:
        personMusic = sorted(personMusic)
        musicOver50 = musicOver50 + personMusic

        musicOver50List[person['name']]=personMusic
      #  for x in personMusic:
       #     if artistGenre.has_key(x.lower()) is False:
        #        print x.lower()


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
personLikesList = {}
personLikesPercentList = {}
count = 1

countLoop=0
#goes through every person
for person in musicOver50List.keys():
    personLikes = {
        'Hip Hop':0.0,
        'Rock':0.0,
        'Pop':0.0,
        'Electronic':0.0,
        'Alternative':0.0,
        'Country':0.0,
        'Other':0.0,
    }

    personLikesPercents = {
        'Not classified':0.0,
        'Hip Hop/Pop':0.0,
        'Hip Hop/Alternative':0.0,
        'Hip Hop/Electronic':0.0,
        'Rock/Pop':0.0,
        'Rock/Alternative':0.0,
        'Rock/Electronic':0.0,
        'Country/Pop':0.0,
        'Country/Alternative':0.0,
        'Country/Electronic':0.0
    }
    #goes through every artist in persons like
    for artist in musicOver50List[person]:
        if artistGenre.has_key(artist.lower()):
            genre = artistGenre[artist.lower()]
            count = personLikes[genre]+1
            personLikes[genre] = count
        else:
            count+=1 #do nothing

    hiphopPop = personLikes['Hip Hop'] + personLikes['Pop']
    hiphopAlternative = personLikes['Hip Hop'] + personLikes['Alternative']
    hiphopElectronic = personLikes['Hip Hop'] + personLikes['Electronic']
    rockPop = personLikes['Rock'] + personLikes['Pop']
    rockAlternative = personLikes['Rock'] + personLikes['Alternative']
    rockElectronic = personLikes['Rock'] + personLikes['Electronic']
    countryPop = personLikes['Country'] + personLikes['Pop']
    countryAlternative = personLikes['Country'] + personLikes['Alternative']
    countryElectronic = personLikes['Country'] + personLikes['Electronic']

    if hiphopPop != 0:
        personLikesPercents['Hip Hop/Pop'] = personLikes['Hip Hop']/hiphopPop
    if hiphopAlternative != 0:
        personLikesPercents['Hip Hop/Alternative'] = personLikes['Hip Hop']/hiphopAlternative
    if hiphopElectronic != 0:
        personLikesPercents['Hip Hop/Electronic'] = personLikes['Hip Hop']/hiphopElectronic
    if rockPop != 0:
        personLikesPercents['Rock/Pop'] = personLikes['Rock']/rockPop
    if rockAlternative != 0:
        personLikesPercents['Rock/Alternative'] = personLikes['Rock']/rockAlternative
    if rockElectronic != 0:
        personLikesPercents['Rock/Electronic'] = personLikes['Rock']/rockElectronic
    if countryPop != 0:
        personLikesPercents['Country/Pop'] = personLikes['Country']/countryPop
    if countryAlternative != 0:
        personLikesPercents['Country/Alternative'] = personLikes['Country']/countryAlternative
    if countryElectronic != 0:
        personLikesPercents['Country/Electronic'] = personLikes['Country']/countryElectronic


    personLikesList[person]=personLikes
    personLikesPercentList[person]=personLikesPercents
    count+=1
    countLoop+=1

print countLoop
#print personLikesList
print len(personLikesList)
print len(personLikesPercentList)
with open('JayBensalFriendData.txt', 'w') as outfile:
    json.dump(personLikesList, outfile, indent=4)

with open('JayBensalFriendDataPercents.txt', 'w') as outfile:
    json.dump(personLikesPercentList, outfile, indent=4)