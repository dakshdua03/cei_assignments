# Q6. Write a Python program that write data in csv file using pandas of ISS Location with timestamp min 100 records
# Use this url to get the data of ISS
# (Url: http://api.open-notify.org/iss-now.json)

import requests
import pandas as pd
import time

url = "http://api.open-notify.org/iss-now.json"
data = []
count = 0  

while count < 100:
    try:
        response = requests.get(url)
        iss_data = response.json()
        
        timestamp = iss_data['timestamp']
        latitude = iss_data['iss_position']['latitude']
        longitude = iss_data['iss_position']['longitude']
        
        data.append([timestamp, latitude, longitude])
        count += 1
        
        print(f"Record {count} fetched successfully")
    
    except Exception as e:
        print(f"Error fetching record {count + 1}: {e}")


df = pd.DataFrame(data, columns=['Timestamp', 'Latitude', 'Longitude'])
df.to_csv('day2\\iss_location.csv', index=False)

print("100 records fetched successfully and saved to iss_location.csv")
