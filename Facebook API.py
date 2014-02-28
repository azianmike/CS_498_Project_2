__author__ = 'michaelluo'

from urllib2 import urlopen
import json

testOpen = urlopen('https://graph.facebook.com/563700600')  #my own ID
testOpenJSON = json.load(testOpen)
print testOpen
print testOpenJSON

testOpenWithFields = urlopen('https://graph.facebook.com/563700600?fields=id,name')
testOpenJSONFields = json.load(testOpenWithFields)
print testOpenJSONFields