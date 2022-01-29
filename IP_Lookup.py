import requests
import json
import pandas as pd

filename = "IP.csv"
df = pd.read_csv("C:\\Users\\ayamr\\Documents\\Coding\\Freelance\\IP.csv")
IP_city = []
IP_state = []

for ip in df:
    # IP address to test
    ip_address = 'ip'
    # URL to send the request to
    request_url = 'https://geolocation-db.com/jsonp/' + ip_address
    # Send request and decode the result
    response = requests.get(request_url)
    result = response.content.decode()
    # Clean the returned string so it just contains the dictionary data for the IP address
    result = result.split("(")[1].strip(")")
    # Convert this data into a dictionary
    result  = json.loads(result)
    IP_city.append(result['city'])
    IP_state.append(result['state'])
# Format city and state into csv columns
df['City'] = IP_city
df['State'] = IP_state
df.to_csv('C:\\Users\\ayamr\\Documents\\Coding\\Freelance\\new_IP.csv')
print(df)

