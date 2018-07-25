'''
Created on Jul 12, 2018

@author: josephginsberg
'''
import requests
from bs4 import BeautifulSoup
import numpy

URL = 'http://aleph.nli.org.il/F/J1TRXLHH6T5I89MGFLJ2VYCI798A6PBJ3J7RTT5HD3NC5DIHDQ-07377?func=direct&doc_number=000135415&'
URL += 'format=001'
URL = 'http://aleph.nli.org.il/F/J1TRXLHH6T5I89MGFLJ2VYCI798A6PBJ3J7RTT5HD3NC5DIHDQ-07377?func=direct&doc_number=000135415&format=001'
URL = 'http://aleph.nli.org.il/F/R61R8LUHDTVD8XRJYKMA8CR43EKHNN6L5RH6BT1A9DERMRKH1S-00048?func=direct&doc_number=001334493&format=001'
request = requests.get(URL)
parser = BeautifulSoup(request.content, 'html.parser')
#print(parser.get_text())
div = parser.find(id = 'fullRecordView')
if div == None:
    print('Sorry, that information is not availble currently. Try waiting')
    quit()
#print(div)
#print(div.contents)
for desc in div.descendants:
    #print(desc)
    stri = desc.string
    if(stri == '245' or stri == '100' or stri == '260'):
        #print(str)
        for nextPiece in desc.next_siblings:
            if(len(nextPiece.string) > 1):
                print(nextPiece.string)