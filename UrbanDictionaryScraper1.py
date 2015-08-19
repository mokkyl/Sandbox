# -*- coding: utf-8 -*-


from lxml import html
import requests

page = requests.get('http://www.urbandictionary.com/')
tree = html.fromstring(page.text)

print "making tree..."

phrases = tree.xpath('//a[@class="word"]/text()')

print "finding phrases..."

meanings = tree.xpath('//div[@class="meaning"]/text()')

print "finding interesting definitions..."
newmeanings = list([s.replace("\n", "") for s in meanings])


print "cleaning..."


dictionary = dict(zip(phrases, newmeanings))
print "Try to use these in every day conversations: \n", 
for keys, values in dictionary.items():
    print keys, ":", values, "\n"
    
