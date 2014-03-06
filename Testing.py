__author__ = 'michaelluo'

from GenreDictionary import artistGenre

hiphopCount=0
electronic=0
country=0
pop=0
rock=0
alternative=0
count=0
for x in artistGenre:

    if artistGenre[x] == 'Hip Hop':
        hiphopCount+=1
    if artistGenre[x] is 'Electronic':
        electronic+=1
    if artistGenre[x] is 'Country':
        country+=1
    if artistGenre[x] is 'Pop':
        pop+=1
    if artistGenre[x] is 'Rock':
        rock+=1
    if artistGenre[x] is 'Alternative':
        alternative+=1

    count+=1

print 'hip hop '+str(hiphopCount)
print 'electronic '+str(electronic)
print 'country '+str(country)
print 'pop '+str(pop)
print 'rock '+str(rock)
print 'alternative '+str(alternative)
print 'total '+str(hiphopCount+electronic+country+pop+rock+alternative)
print 'total count '+str(count)