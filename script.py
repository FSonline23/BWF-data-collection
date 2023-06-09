import pandas as pd
import requests as re
import numpy as np
import datetime
import json
import argparse
import config
import csv


class API:
    headers = {
        "Accept": "*/*",
        "Content-Type": "application/json",
        "User-Agent": "PostmanRuntime/7.29.2",
        "Accept-Encoding": "gzip, deflate, br",
        "Origin": "https://bwfbadminton.com/",
        "Referer": "https://bwfbadminton.com/"
    }

    def __init__(self, apiEndPoint, apiCredentials, method, **kwargs):
        self.apiEndPoint = apiEndPoint
        self.apiCredentials = apiCredentials
        self.method = method
        self.kwargs = kwargs
        self.appendAuthHeaders()

    def __str__(self):
        variablesConcatStr = ""
        for key, value in self.kwargs.items():
            variablesConcatStr = variablesConcatStr + "Key={}, Value={}\n".format(key, value)
        return f"API Endpoint: {self.apiEndPoint}\nAPI Key: {self.apiKey}\nVariables:\n{variablesConcatStr}"
    
    def appendAuthHeaders(self):
        if len(self.apiCredentials) < 128:
            self.headers["ApiKey"] = self.apiCredentials
        else:
            self.headers["Authorization"] = "Bearer " + self.apiCredentials
        return

    def fetch_data(self):
        data = {}
        for key, value in self.kwargs.items():
            data[key] = value
        json_data = data

        if self.method == "GET":
            res =re.get(
                url=self.apiEndPoint,
                headers=self.headers,
                params=json_data
            )
            if res.status_code == 200:
                return res.json()
            else:
                print("Failed calling API!")
                print(res.text)
                exit()
        elif self.method == "POST":
            res = re.post(
                url=self.apiEndPoint,
                headers=self.headers,
                json=json_data
            )
            if res.status_code == 200:
                return res.json()
            else:
                print("Failed calling API!")
                print(res.text)
                exit()


def parseScriptArguments():
    description = "This is a python script to automate data collection and cleaning of World Athletics results retrieved from World Athletics website's backend API."
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("-ath", "--Athlete", help="Define Athlete for Search")
    parser.add_argument("-disc", "--Discipline", help="Define Discipline for Search")
    parser.add_argument("-o", "--OutputName", help="Define Output file name of Scrapped Results (without '.xlsx' extension)")
    parser.add_argument("-tf", "--TargetFileName",
                        help="Target File Name (default is cleanedResults.csv) for performing filtering operations on using namelist.csv and discipline supplied. Please include '.csv' extension in argument.")
    parser.add_argument("-nl", "--NameListCSV",
                        help="Name List CSV file (default is namelist.csv) that will be used for performing filtering operations on cleaned results data. Please include '.csv' extension in argument and ensure '* namelist.csv' naming convention.")
    parser.add_argument("-c", "--CompileIntoFolder", action='store_true',
                        help="Compile filtered namelist CSV and filtered data into a folder specified by user. Please ensure argument is a legal folder name.")
    parser.add_argument("-filteronly", "--FilterOnly", action='store_true',
                        help="Filter existing cleanedResults.csv by discipline specified. Scrapping will not be performed prior.")
    parser.add_argument("-scrapeonly", "--ScrapeOnly", action='store_true',
                        help="Scape and clean data only. Will not perform filtering by discipline or namelist.csv.")
    parser.add_argument("-search", "--SearchAthlete", action='store_true',
                        help="Search athlete using API and return results as searchResults.csv.")
    parser.add_argument("-append", "--AppendToCleanedResults", action='store_true',
                        help="Append search results to cleanedResults.csv.")
    parser.add_argument("-athCSV", "--AthleteCSV", help="Define Athlete CSV file for searches.")
    parser.add_argument("-countryCSV", "--countryCSV", help="Define Country CSV file for searches and scrapping.")
    args = parser.parse_args()

    return


def main():
    config.importAPIs()
    pass
    return


if __name__ == "__main__":
    main()