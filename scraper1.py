'''
Created on Jul 12, 2018

@author: josephginsberg
'''
import requests
from bs4 import BeautifulSoup
import argparse

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

def main(args):
    x = MARCs(args)
    for i in x:
        print i + ': ' + x[i]
 
def parse_arguments():
    parser = argparse.ArgumentParser(description="Accept arguments")
    parser.add_argument('-url', '--url', required=True)
    return parser.parse_args()
     
if __name__ == '__main__':
    args = parse_arguments()
    main(args)
