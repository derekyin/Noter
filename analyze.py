
import argparse
import json
import sys

from googleapiclient import discovery
import httplib2
from oauth2client.client import GoogleCredentials


def get_service():
    credentials = GoogleCredentials.get_application_default()
    scoped_credentials = credentials.create_scoped(
        ['https://www.googleapis.com/auth/cloud-platform'])
    http = httplib2.Http()
    scoped_credentials.authorize(http)
    return discovery.build('language', 'v1beta1', http=http)


def get_native_encoding_type():
    if sys.maxunicode == 65535:
        return 'UTF16'
    else:
        return 'UTF32'


def analyze_entities(text, encoding='UTF32'):
    body = {
        'document': {
            'type': 'PLAIN_TEXT',
            'content': text,
        },
        'encodingType': encoding,
    }

    service = get_service()

    request = service.documents().analyzeEntities(body=body)
    response = request.execute()

    return response

#if __name__ == '__main__':    
def processText(rawText):
    #rawText = "this is a test to see if you are smart in canada or the united states of america. Donald Trump is fat and white and stupid. Donald Trump is not intelligent because Tesla. Donald Trump. Donald Trump. Donald Trump."
    #print rawText
    result = analyze_entities(rawText, get_native_encoding_type())

    counter = {}
    position = {}

    for key in result["entities"]:
        for innerkey in key["mentions"]:
            word = str(innerkey["text"]["content"]);
            pos = str(innerkey["text"]["beginOffset"])
            if (counter.has_key(word)):
                counter[word] = str(int(counter[word]) + 1)
                position[word].append(pos)
            else:
                counter[word] = "1"
                lst = []
                lst.append(pos)
                position[word] = lst;
            

    num = len(counter)
    print num
    curSum = 0
    for key in counter:
        curSum = curSum + int(counter[key])
        #print curSum
    if (num != 0):
        average = float(curSum*1.0/num)
    else:
        average = 0
    print average
    #print curSum
    #print average
    #list of json objects to return
    lst = []
    keyword = {}
    #loop through hashmap to collect data of keywords and
    #package them into JSON
    #print(json.dumps(result, indent=2))
    for key in counter:
        importance = 0
        if float(counter[key]) > average:
            importance = 2
        elif float(counter[key]) == average:
            importance = 1
        elif float(counter[key]) < average:
            importance = 0
        print counter[key] < average
        print average
        keyword = {
            "word":key,
            "position":position[key],
            "highlight":importance
        }
        lst.append(keyword)
    print(json.dumps(lst, indent=2))
    
    return lst
    #for key in counter:
    #    print key
    #    print (counter[key])
