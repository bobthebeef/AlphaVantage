# Main driver for calling the alphavantage intraday stock market API: https://www.alphavantage.co/documentation/
# Ultimate goal is to create an app that will accept input from users and display output data for the specific stock selected
# 
#
import requests
import json

def CallAPI(ticker,interval,key):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+ticker+'&interval='+interval+'&apikey='+key
    print(url) 
    response = requests.get(url)
    return response.json()

def HandleResponse():
    pass

def main():
    #TODO: replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    response = CallAPI("IBM","5min","demo")
    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    print(response)
    pass

if __name__ == '__main__':
    main()
