# Documentation
This is a script for scrapping results from <a href="">World Table Tennis Federation</a> website.
<hr>

## Requirements
<pre>
    <code>
    pip install -r requirements.txt
    </code>
</pre>
<hr>

## Installation
These are the instructions for installation:

<hr>

## What does the script do?

API Endpoints and authentication:

<table>
    <thead>
        <td>Endpoint</td>
        <td>Auth Type</td>
        <td>Credentials</td>
        <td>Description</td>
    </thead>
    <tbody>
        <tr>
            <td>
                <a href="https://wttapigateway-new.azure-api.net/prod/api/cms/GetPlayerListWithName">
                    https://wttapigateway-new.azure-api.net/prod/api/cms/GetPlayerListWithName
                </a>    
            </td>
            <td rowspan="2">Bearer Token</td>
            <td rowspan="2" width="25%">eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ilg1ZVhrNHh5b2pORnVtMWtsMll0djhkbE5QNC1jNTdkTzZRR1RWQndhTmsifQ.eyJpc3MiOiJodHRwczovL3dvcmxkdGFibGV0ZW5uaXNiMmMuYjJjbG9naW4uY29tL2MxMzg4YzFiLTJlMTMtNDQzOS1hOTlkLTM5OTM1YWNmMDAwOS92Mi4wLyIsImV4cCI6MTY3ODI2MjMwMCwibmJmIjoxNjc4MTc1OTAwLCJhdWQiOiIyNGNkMDdjYS1kZjcwLTQ5ZWEtYjVlMC03MGRhY2JhMjk0NzAiLCJvaWQiOiJiZDU2MGQxNy1lMGEyLTQyNGQtODM0OC00NGRmMDk4ZTRkYTAiLCJzdWIiOiJiZDU2MGQxNy1lMGEyLTQyNGQtODM0OC00NGRmMDk4ZTRkYTAiLCJjb3VudHJ5IjoiU0dQIiwibmFtZSI6IktpbmcgWWV1bmcgTGVlIiwiZXh0ZW5zaW9uX2RvYiI6IjAxLzI4LzE5OTcgMTY6MDA6MDAiLCJleHRlbnNpb25fZW5hYmxlX3B1c2hfbm90aWZpY2F0aW9ucyI6ZmFsc2UsImV4dGVuc2lvbl9HZW5kZXIiOiJNIiwiZ2l2ZW5fbmFtZSI6IktpbmcgWWV1bmciLCJleHRlbnNpb25fTmFtZUZvcm1hdCI6IkZpcnN0TmFtZUZpcnN0IiwiZXh0ZW5zaW9uX05hdGlvbmFsaXR5IjoiU0dQIiwiZXh0ZW5zaW9uX3Bob25lX251bWJlcl9jb3VudHJ5Y29kZSI6IjY1IiwiZXh0ZW5zaW9uX3ByaXZhY3lwb2xpY3lfYWdyZWVkIjp0cnVlLCJmYW1pbHlfbmFtZSI6IkxlZSIsImV4dGVuc2lvbl90ZXJtc19hZ3JlZWQiOnRydWUsImVtYWlscyI6WyJraW5neWV1bmcxMjlAaG90bWFpbC5jb20iXSwidGZwIjoiQjJDXzFfV3R0X1dlYl9TaWduSW4iLCJub25jZSI6ImFrNDVMV3R6VG1kTlgyOVhOMmhtTUdkNWVtRkpjRkpmU2kxVGZtbEliVzVQVTNkMmVrdEhhelF3UkdOUCIsInNjcCI6InByb2ZpbGUgb3BlbmlkIHVzZXJfaW1wZXJzb25hdGlvbiIsImF6cCI6IjI0Y2QwN2NhLWRmNzAtNDllYS1iNWUwLTcwZGFjYmEyOTQ3MCIsInZlciI6IjEuMCIsImlhdCI6MTY3ODE3NTkwMH0.csWOvFkhqUqmGlu1I9FY3YnIFYl9X3rYlsFEWlttbWIsgQSpT7zzC6noxW0Esm35GN9rCnUdYZDUdbY5yDM0gSo04gxj9_x2QmuxGTtnb4kdMtGGaxJ3HEcl3opphCSu6Jp_sW_5e8t0a8bLAuaU4A1HzygY0xMgdst94IqguaW62pUAAFcyauqJXhWVOpFWoBxPrbUpfHP7dBbniB7lnPHmwBp2Orx6aiMSqmqyXZ2Dv3WxurSI2J3ytoRtQvYxTaEwDZvI_xUar6L4FgUSfbHhav2khFdx5o8529oymQsy0QpKw0LPWIhJ51AAc1ARlmf8BL2tF4WatLsHQDvKLw</td>
            <td>Get Player List with Name</td>
        </tr>
        <tr>
            <td>
                <a href="https://wttapigateway-new.azure-api.net/prod/api/cms/GetPlayersListByFilters/1/0">
                    https://wttapigateway-new.azure-api.net/prod/api/cms/GetPlayersListByFilters/1/0
                </a>    
            </td>
            <td>
                Search players using the following json arguments in request body.
                <pre>
                    <code>
                        {"searchText":"Singapore"}
                    </code>
                </pre>
            </td>
        </tr>
        <tr>
            <td>
                <a href="https://wttapigateway-new.azure-api.net/ttu/Players/GetPlayers">
                    https://wttapigateway-new.azure-api.net/ttu/Players/GetPlayers
                </a>    
            </td>
            <td rowspan="2">API Key</td>
            <td rowspan="2">2bf8b222-532c-4c60-8ebe-eb6fdfebe84a</td>
            <td>
                Get ALL players on IF website
            </td>
        </tr>
        <tr>
            <td>
                <a href="https://wttapigateway-new.azure-api.net/ttu/Stats/Players/GetStatsByPlayer">
                    https://wttapigateway-new.azure-api.net/ttu/Stats/Players/GetStatsByPlayer
                </a>    
            </td>
            <td>
                Get stats of specified player ittfId in GET parameter. StartDate and EndDate can be defined in the format "yyyy-mm-dd".
            </td>
        </tr>
        <tr>
            <td>
                <a href="https://wttapigateway-new.azure-api.net/ttu/Rankings/GetRankingIndividuals">
                    https://wttapigateway-new.azure-api.net/ttu/Rankings/GetRankingIndividuals
                </a>    
            </td>
            <td>
                Get ranking of specified player ittfId in GET parameter.
            </td>
        </tr>
    </tbody>
</table>

Understanding the WTTF API Model

<i>Please note that the structure may change in the future</i>

The results for each competition event are split by disciplines (for e.g. Men's doubles). Each event discipline is tied to a document code (for e.g. TTEMDOUBLES-----------FNL-000100----------). In order to query results from a specific event, we need to first identify the eventId. This can be done by using the search events by date API end point to retrieve a list of events from a date range argument (https://ittf-admin-api.azurewebsites.net/api/calendar/events). After obtaining the eventId, doc code must be acquired with another API end point (https://wttapigateway-new.azure-api.net/prod/api/cms/GetOfficialResult?EventId[EVENTID]&DocumentCode=TTE) using the eventId as argument to obtain the specific match results. 