import Authentication.login,tweepy, Status.MakeStatus
import Logging.loggerCode
import QueryLogic.QueryHandler
#Note: This is not the version of main used on the server, however the functions used are identical to the ones used on the server.
logEvents = Logging.loggerCode
credVal = 0
allMentions = []
noRequests = False
try:
    login = Authentication.login.loginFunction()
    logEvents.updateLog("Bot logged in")
except:
    logEvents.updateLog("Issue with login variable")

callTweepy = tweepy.API(login)
credVal = callTweepy.verify_credentials()
if credVal == False:
    logEvents.updateLog("Authentication Error")
else:
    logEvents.updateLog("Authentication was valid")
i = 0
while i != 4:
    continueRun = QueryLogic.QueryHandler.getMentions(callTweepy,allMentions)
    if(continueRun==0):
        noRequests = True
        break
    if(len(continueRun)==0):
        noRequests = True
        break
    if(len(continueRun)<20):
        break
    i+=1
userList = allMentions
if(type(userList)==int):
    exit(0)
if(noRequests==True):
    exit(3)
Status.MakeStatus.makePost(callTweepy, userList)
exit(4)

