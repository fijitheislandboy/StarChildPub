import spotipy,os
import Logging.loggerCode
from spotipy.oauth2 import SpotifyClientCredentials
from random import randint

SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']

def getDMs(InheritedapiFunction):
    messageList = InheritedapiFunction.list_direct_messages(100)
    for i in range (0,len(messageList)-1):
        workValue = messageList[i]
        creationAttribute = getattr(workValue,'message_create')
        messageFrom = creationAttribute['sender_id']
        if(messageFrom =='1377922691697668096'):
            messageText = creationAttribute['message_data']['text']
            messageText = int(messageText)
            return messageText
        else:
         i = i + 1
    return 0

def getMentions(apiFunction, largeMentionList): #Public
    searchFrom = getDMs(apiFunction)
    listMentions = apiFunction.mentions_timeline(searchFrom)
    if(len(listMentions)==0):
        Logging.loggerCode.updateLog("There were no new mentions")
        return 0
    else:
        largeMentionList.append(listMentions)
    toSend = getattr(listMentions[0],'id_str')
    if(toSend!=searchFrom):
        dmSuccess = sendDMToSelf(apiFunction,toSend)
        if(dmSuccess==0):
            return listMentions
        else:
            timesAttempted = 0
            while((dmSuccess!=0) and (timesAttempted != 10)):
                dmSuccess = (apiFunction,searchFrom)
                timesAttempted+=1
            return -1
    if(toSend==searchFrom):
        return 0

def sendDMToSelf(SendApiFunction,tweetId):
    Logging.loggerCode.updateLog("Message send attempt with content: " + tweetId)
    try:
        SendApiFunction.send_direct_message(1377922691697668096,tweetId)
    except:
        Logging.loggerCode.updateLog("Message send attempt with content: " + tweetId + " failed.")
        return -1
    Logging.loggerCode.updateLog("Message send attempt with content: " + tweetId + " successful.")
    return 0


def spotifyFunction():
    authenticate = SpotifyClientCredentials()
    starchild = spotipy.Spotify(auth_manager=authenticate)

    myPlaylist = starchild.playlist('')#insert playlist name here
    playlistTracks = myPlaylist['tracks']
    songs = playlistTracks['items']
    while playlistTracks['next']:
        playlistTracks = starchild.next(playlistTracks)
        for item in playlistTracks['items']:
            songs.append(item)
    songIndex = randint(0,len(songs))
    songTitle = songs[songIndex]['track']['name']
    songURL= songs[songIndex]['track']['external_urls']['spotify']
    songArtist = songs[songIndex]['track']['album']['artists'][0]['name']
    return songTitle,songURL,songArtist
