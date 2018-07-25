'''
Created on Jul 12, 2018

@author: josephginsberg
'''
import requests
from bs4 import BeautifulSoup

def MARCs (URL):
    URL += 'format=001'
    request = requests.get(URL)
    parser = BeautifulSoup(request.content, 'html.parser')
    div = parser.find(id = 'fullRecordView')
    if div == None:
        print('Sorry, that information is not availble currently. Try waiting a little bit.')
        quit()
    dic = {}
    for desc in div.descendants:
        stri = desc.string
        if(stri == '24510'):
            for nextPiece in desc.next_siblings:
                if(len(nextPiece.string) > 1):
                    dic['Description'] = str(nextPiece.string.encode('utf-8'))
        elif(stri == '100'):
            for nextPiece in desc.next_siblings:
                if(len(nextPiece.string) > 1):
                    dic['Author'] = str(nextPiece.string.encode('utf-8'))  
        elif(stri == '260'):
            for nextPiece in desc.next_siblings:
                if(len(nextPiece.string) > 1):
                    dic['Printings'] = str(nextPiece.string.encode('utf-8'))          
    return dic

def main():
    url = 'http://aleph.nli.org.il/F/R61R8LUHDTVD8XRJYKMA8CR43EKHNN6L5RH6BT1A9DERMRKH1S-00048?func=direct&doc_number=001334493&'
    x = MARCs(url)
    for i in x:
        print i + ': ' + x[i]
     
if __name__ == '__main__':
    main()
