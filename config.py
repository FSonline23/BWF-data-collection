import json

countries_list = [
    "Singapore",
    "Malaysia",
]

namelistCSV ="namelist.csv"

outputCSVFileName = "output.csv"
outputXlsxFileName = "output.xlsx"


def importAPIs(apiJSONfile="api.json"):
    global APIgetPlayerWithNameList
    global APIsearchPlayer
    global APIgetAllPlayers
    global APIgetStatsByPlayers
    global APIgetRankingIndividuals
    global APIgetEventsByDate
    global APIgetEventDocCode
    global APIgetDetailedResultsByEvent

    global dictAPIkey
    global dictAPIMethod

    apiJSONdata = json.load(open(apiJSONfile))
    APIgetPlayerWithNameList = apiJSONdata['apiEndPoint_getPlayerList']
    APIsearchPlayer = apiJSONdata['apiEndPoint_searchPlayer']
    APIgetAllPlayers = apiJSONdata['apiEndPoint_getAllPlayers']
    APIgetStatsByPlayers = apiJSONdata['apiEndPoint_getStatsByPlayer']
    APIgetRankingIndividuals = apiJSONdata['apiEndPoint_getRankingIndividuals']
    APIgetEventsByDate = apiJSONdata['apiEndPoint_getEventsByDate']
    APIgetEventDocCode = apiJSONdata['apiEndPoint_getEventDocCode']
    APIgetDetailedResultsByEvent = apiJSONdata['apiEndPoint_getDetailedResultsByEvent']

    dictAPIkey = {}
    dictAPIkey[APIgetPlayerWithNameList] = apiJSONdata['bearerToken']
    dictAPIkey[APIsearchPlayer] = apiJSONdata['bearerToken']
    dictAPIkey[APIgetAllPlayers] = apiJSONdata['apiKey']
    dictAPIkey[APIgetStatsByPlayers] = apiJSONdata['apiKey']
    dictAPIkey[APIgetRankingIndividuals] = apiJSONdata['apiKey']
    dictAPIkey[APIgetEventsByDate] = apiJSONdata['apiKey']
    dictAPIkey[APIgetEventDocCode] = apiJSONdata['apiKey']
    dictAPIkey[APIgetDetailedResultsByEvent] = apiJSONdata['apiKey']

    dictAPIMethod = {}
    dictAPIMethod[APIgetPlayerWithNameList] = "GET"
    dictAPIMethod[APIsearchPlayer] = "POST"
    dictAPIMethod[APIgetAllPlayers] = "GET"
    dictAPIMethod[APIgetStatsByPlayers] = "GET"
    dictAPIMethod[APIgetRankingIndividuals] = "GET"
    dictAPIMethod[APIgetEventsByDate] = "POST"
    dictAPIMethod[APIgetEventDocCode] = "GET"
    dictAPIMethod[APIgetDetailedResultsByEvent] = "GET"
    return