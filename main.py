from settings import *
from urllib import parse
import requests
import json


def buildFlightParameters(parameters):
    fareClass = parameters['fareClass']
    flightParameters = {
        'segment': '1',
        'pointOfSale': 'QkFC',
        'flightInfo': [{
            "flight": [{
                "fareClass": fareClass,
                "flightNumber": parameters['flightNumber'],
                "airlineCodeOperating": "WS",
                "operatingFlightNumber": parameters['flightNumber'],
                "airlineCodeMarketing": "WS",
                "departureDateTime": parameters['departureDateTime'],
                "arrivalDateTime": parameters['arrivalDateTime'],
                "arrival": parameters['arrivingAirportCode'],
                "departure": parameters['departingAirportCode']
            }]
        }]
    }
    return flightParameters


def printMap(parameters):
    print("Premium Ticket Holders...")
    # premium
    parameters['fareClass'] = "R"
    flightParameters = buildFlightParameters(parameters)
    seatmap = getMap(flightParameters)

    print("Basic Economy Ticket Holders...")
    # economy
    parameters['fareClass'] = "B"
    flightParameters = buildFlightParameters(parameters)
    seatmap = getMap(flightParameters)

    # iterate through seats // make sure you specify $0 for Premium ticket holders


def getMap(parameters):

    # http get seatmap
    url = WESTJET_URLS["host"] + WESTJET_URLS["seatmap"] + "?" + parse.urlencode(parameters).replace("%27", "%22")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.80 Safari/537.36',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, defalte',
        'Connection': 'keep-alive'
    }
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    if(response.status_code != 200):
        print("Unable to retreive flight info. Response: " + response.text)
    else:
        rows = data.get("aircraft").get("deck").get("cabin").get("rows")
        for row in rows:
            seats = row.get("seats")
            for seat in seats:
                available = "NOT AVAILABLE"
                if(seat.get("occupied") is False and seat.get("characteristics").get("NO_SEAT", False) is False and seat.get("characteristics").get("BLOCKED_SEAT", False) is False):
                    available = "AVAILABLE"
                print("Seat: {0} \tPrice: ${1} \t{2}".format(seat["seatNumber"], seat.get("price"), available))
        print("\n")


def main():

    # flightNumber = "1755"
    # departingAirportCode = "SNA"
    # arrivingAirportCode = "YVR"
    # departureDateTime = "2019-08-18T14:55:00"
    # arrivalDateTime = "2019-08-18T17:42:00"
    flightNumber = input('flight number (ex. 1755): ')
    departingAirportCode = input('departing airport code (ex. SNA): ')
    arrivingAirportCode = input('arriving airport code (ex. YVR): ')
    departureDateTime = input('departure datetime (ex. 2019-08-18T14:55:00): ')
    arrivalDateTime = input('arrival datetime (ex. 2019-08-18T17:42:00): ')
    parameters = {
        'flightNumber': flightNumber,
        'departingAirportCode': departingAirportCode,
        'arrivingAirportCode': arrivingAirportCode,
        'departureDateTime': departureDateTime,
        'arrivalDateTime': arrivalDateTime
    }
    print("Seatmap for Flight WS{0} \t {1} to {2}".format(flightNumber, departingAirportCode, arrivingAirportCode, departureDateTime, arrivalDateTime))
    printMap(parameters)


if __name__ == '__main__':
    main()
