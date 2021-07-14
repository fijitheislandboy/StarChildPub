import Logging.loggerCode
import QueryLogic.QueryHandler

def makePost(apiFunction,userNameList):
    if(len(userNameList)==0):
        return 0
    for i in range(0,len(userNameList[0])):
        songTitle, returnLink, artistName = QueryLogic.QueryHandler.spotifyFunction()
        userName = getattr(userNameList[0][i],'author','screen_name')
        screenName = getattr(userName,'screen_name')

        statusText = "Here is your recommendation @"+screenName+". It's "+ songTitle + " by "+ artistName + "!\n" + returnLink

        apiFunction.update_status(statusText)
        Logging.loggerCode.updateLog("New status was posted with text " + statusText)
        i+=1
    return 0
