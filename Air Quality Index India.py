import pandas as pd
import pygsheets
import sys
import json
import google.auth

if (len(sys.argv) == 3):
    print('Number of arguments:', len(sys.argv), 'arguments.')
    if (len(str(sys.argv[1])) > 0 and len(str(sys.argv[2])) > 0):
        print('Two arguments passed i.e. API Key', len(str(sys.argv[1])), '& Google Credentials', len(str(sys.argv[2])), '. Setting up API Key.')
        apiKey = str(sys.argv[1])
        secret_dict = str(sys.argv[2])

        # SCOPES = ('https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive')
        # service_account_info = json.loads(secret_dict)
        # my_credentials = google.oauth2.service_account.Credentials.from_service_account_info(service_account_info, scopes=SCOPES)
        
        # root = pd.read_csv('https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69?api-key='+apiKey+'&format=csv&offset=0&limit=10000')
        # print("-----------------Downloaded--------------------")
        # root.rename(columns={'id': 'ID', 'country': 'Country', 'state': 'State', 'city': 'City', 'station': 'Station', 'last_update': 'Reading Date', 'pollutant_id': 'Pollutant', 'pollutant_min': 'Min_Value', 'pollutant_max': 'Max_Value', 'pollutant_avg': 'Avg_Value', 'pollutant_unit': 'Unit'}, inplace=True)
        # print("-----------------Renamed Columns--------------------")

        # root['Reading Date'] = pd.to_datetime(root['Reading Date'])
        # print("-----------------Changed Date Format--------------------")

        # root['State'] = root['State'].replace(to_replace=r'_', value=' ', regex=True)
        # print("-----------------Cleaned State (remove _ from State value)--------------------")
        # root['Station'] = root[['City','Station']].apply(lambda x: x.Station[0:x.Station.find(', '+x.City)], axis=1)
        # print("-----------------Cleaned Station (remove redundant City value)--------------------")

        # root = root.fillna(0.0)

        # print(root.info())
        # print(root.head())
        # print("-----------------Processed--------------------")

        # client = pygsheets.authorize(custom_credentials=my_credentials)
        # print("-----------------Authorized--------------------")
        # sheet = client.open('Air Quality Index India Feed')
        # print("-----------------Sheet Opened------------------")
        # wks = sheet[0]
        # wks.clear("*")
        # print("-----------------First Sheet Accessed----------")
        # wks.set_dataframe(root,(1,1))
        # print("-----------------Data Updated------------------")
    else:
        print('Empty arguments passed i.e. API Key', len(str(sys.argv[1])), '& Google Credentials', len(str(sys.argv[2])), '. Skipping execution.')

else:
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Only 2 arguments are required i.e. API Key & Google Credentials. Skipping execution.')

