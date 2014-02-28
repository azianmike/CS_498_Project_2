__author__ = 'michaelluo'

from urllib2 import urlopen
import json

testOpen = urlopen('https://graph.facebook.com/563700600')
testOpenJSON = json.load(testOpen)
print testOpen
print testOpenJSON
