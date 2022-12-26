import ast
from typing import List
from os import listdir

#obtain streaming information
def getMyStreaming(path: str = '../streaming') -> List[dict]:
    streamingFiles = ['../streaming/' + i for i in listdir(path)
                      if i.split('.')[0][:-1] == 'StreamingHistory']
    
    allSongs = []
    for file in streamingFiles:
        with open(file, 'r', encoding='UTF-8') as i:
            newSongs = ast.literal_eval(i.read())
            allSongs += [song for song in newSongs]
    
    return allSongs

#obtain features information    
def songFeatures(myStreamings) -> List[dict]:
    #TODO:
    return 1 

#convert features information into Json File
def songToJSON(myStreamings) -> List[dict]:
    #TODO:
    return 1

#get amount of times I listened to each song
def songAmount(myStreamings): # return type is a dictionary of dictionaries
    dic = {}
    for streaming in myStreamings:
        if streaming['trackName'] not in dic:
            dic[streaming['trackName']] = {}
            dic[streaming['trackName']]['timesPlayed'] = 1
            dic[streaming['trackName']]['timePlayed'] = streaming['msPlayed']
        else:
            dic[streaming['trackName']]['timesPlayed'] += 1
            dic[streaming['trackName']]['timePlayed'] += streaming['msPlayed']
    return dic

#sort streaming by time played
def sortTimePlayed(songDict): # 
    sortDict = sorted(songDict.items(), key=lambda x:x[1]['timePlayed'], reverse=True)
    convertDict = dict(sortDict)
    return convertDict
    
    
# sort streaming by times played   
def sortTimesPlayed(songDict):
    #TODO:
    sortDict = sorted(songDict.items(), key=lambda x:x[1]['timesPlayed'], reverse=True)
    convertDict = dict(sortDict)
    return convertDict

def wrapped():
    #TODO
    return 1

     
if __name__ == '__main__':
    myStreaming = getMyStreaming() # creating a myStreaming list of dictionaries
    songDict = songAmount(myStreaming) # creating a dong dictionary (dict of dicts)
    sortTime = sortTimePlayed(songDict)
    sortTimes = sortTimesPlayed(songDict)