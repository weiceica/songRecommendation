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

#convert features information into Json File

#get amount of times I listened to each song

if __name__ == '__main__':
    myStreaming = getMyStreaming()
    print(myStreaming)