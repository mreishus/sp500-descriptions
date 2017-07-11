#!env python3

import requests
import json

tiingoAuth = '1234'

headers = {
    'Content-Type': 'application/json',
    'Authorization' : 'Token ' + tiingoAuth
}
requestResponse = requests.get("https://api.tiingo.com/api/test/", headers=headers)
print(requestResponse.json())

def getDescription(ticker):
    headers = {
        'Content-Type': 'application/json',
        'Authorization' : 'Token ' + tiingoAuth
    }
    try:
        output = ''
        requestResponse = requests.get("https://api.tiingo.com/tiingo/daily/" + ticker, headers=headers)
        j = requestResponse.json()
        output = j['description']
    except:
        output = ''
    return output


print("Hello")
#print(getDescription("AAPL"))

import csv
reader = csv.reader(open('constituents.csv', 'r'))
#reader = csv.reader(open('trimmed.csv', 'r'))
writer = csv.writer(open('output.csv', 'w'))
headers = next(reader)
headers.append("Description")
writer.writerow(headers)
for row in reader:
    row.append(getDescription(row[0]))
    writer.writerow(row)
