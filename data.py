import pandas as pd
import requests 
from io import StringIO
import psycopg2

ROOT = "https://data.cityofnewyork.us/resource/h9gi-nx95.json" #use data from opendata
LIMIT = 10 # 1000000
YEAR = 2024
STARTMONTH = 1
STARTDATE = 1
ENDMONTH = 4
ENDDATE = 13
URL = f"{ROOT}?$limit={LIMIT}&$where=crash_date between '{YEAR}-{STARTMONTH}-{STARTDATE}T00:00:00' and '{YEAR}-{ENDMONTH}-{ENDDATE}T23:59:59'"

response = requests.get(URL)

#call API by this function response.text
# read JSON-formatted data into a DataFrame.
# Create a StringIO object to wrap the JSON string
json_string = StringIO(response.text)
df = pd.read_json(json_string)
df = df.dropna(subset=['latitude', "longitude", "location"], how="any")


df["crash_date"] = pd.to_datetime(df["crash_date"])
df["crash_date_year"] = df["crash_date"].dt.year
df["crash_date_month"] = df["crash_date"].dt.month

#converting date to human readable format
df["crash_date_date"] = df["crash_date"].dt.strftime('%Y-%m-%d %H:%M:%S')


#hour,min,sec
df['crash_time_hour'] = df["crash_time"].dt.hour
df['crash_time_minute'] = df["crash_time"].dt.minute
df['crash_time_second'] = df["crash_time"].dt.second


# List of column names
column_names = [
    'location',
    'latitude',
    'longitude',
    'crash_date',
    'crash_date_year',
    'crash_date_month',
    'crash_date_date',
    # 'crash_time',
    'crash_time_hour',
    'crash_time_minute',
    'crash_time_second',
    'number_of_persons_injured',
    'number_of_persons_killed',
    'number_of_pedestrians_injured',
    'number_of_pedestrians_killed',
    'number_of_cyclist_injured',
    'number_of_cyclist_killed',
    'number_of_motorist_injured',
    'number_of_motorist_killed'
]

# Create a new DataFrame with only the specified columns
df_filtered = df[column_names]

# df['number_of_persons_injured'] = df_filtered['number_of_persons_injured'].apply(lambda x : x * 6 + 1)

#filtered data returned to data.json file
df_filtered.to_json('data.json', index=False)
# df.to_json('originaldata.json', index=False)
df.to_csv('data.csv', index=False)

