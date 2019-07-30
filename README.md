# westjet-seatmap
this is a simple console app written in python3

given appropriate parameters, app will return seat price and availability.

app performs 2 HTTP GET requests to [https://apiw.westjet.com/bookingservices/seatmap] -- first request for First Class seatmap, second request to retrieve Basic Economy seatmap

to reduce params necessary, we could consider doing a flight lookup based on the flight number and departure date

data is returned as json but no further serialization in datatables is done. goal here is simply a proof of concept.

```
Brian$ python3 main.py
flight number (ex. 1755): 1755
departing airport code (ex. SNA): SNA                         
arriving airport code (ex. YVR): YVR
departure datetime (ex. 2019-08-18T14:55:00): 2019-08-18T14:55:00
arrival datetime (ex. 2019-08-18T17:42:00): 2019-08-18T17:42:00
Seatmap for Flight WS1755 	 SNA to YVR

Premium Ticket Holders...
Seat: 1A 	Price: $0 	AVAILABLE
Seat: 1B 	Price: $0 	NOT AVAILABLE
Seat: 1C 	Price: $0 	AVAILABLE
Seat: 1D 	Price: $N/A 	NOT AVAILABLE
Seat: 1E 	Price: $0 	NOT AVAILABLE
Seat: 1F 	Price: $N/A 	NOT AVAILABLE
Seat: 2A 	Price: $N/A 	NOT AVAILABLE
Seat: 2B 	Price: $0 	NOT AVAILABLE
Seat: 2C 	Price: $N/A 	NOT AVAILABLE
Seat: 2D 	Price: $N/A 	NOT AVAILABLE
Seat: 2E 	Price: $0 	NOT AVAILABLE
Seat: 2F 	Price: $N/A 	NOT AVAILABLE
Seat: 3A 	Price: $N/A 	NOT AVAILABLE
Seat: 3B 	Price: $0 	NOT AVAILABLE
Seat: 3C 	Price: $N/A 	NOT AVAILABLE
Seat: 3D 	Price: $N/A 	NOT AVAILABLE
Seat: 3E 	Price: $0 	NOT AVAILABLE
Seat: 3F 	Price: $N/A 	NOT AVAILABLE


Basic Economy Ticket Holders...
Seat: 4A 	Price: $N/A 	NOT AVAILABLE
Seat: 4B 	Price: $N/A 	NOT AVAILABLE
Seat: 4C 	Price: $N/A 	NOT AVAILABLE
Seat: 4D 	Price: $14.50 	AVAILABLE
Seat: 4E 	Price: $14.50 	AVAILABLE
Seat: 4F 	Price: $14.50 	AVAILABLE
Seat: 5A 	Price: $N/A 	NOT AVAILABLE
Seat: 5B 	Price: $N/A 	NOT AVAILABLE
Seat: 5C 	Price: $N/A 	NOT AVAILABLE
Seat: 5D 	Price: $14.50 	AVAILABLE
Seat: 5E 	Price: $14.50 	AVAILABLE
Seat: 5F 	Price: $14.50 	AVAILABLE
Seat: 6A 	Price: $N/A 	NOT AVAILABLE
Seat: 6B 	Price: $N/A 	NOT AVAILABLE
Seat: 6C 	Price: $N/A 	NOT AVAILABLE
Seat: 6D 	Price: $14.50 	AVAILABLE
Seat: 6E 	Price: $14.50 	AVAILABLE
Seat: 6F 	Price: $14.50 	AVAILABLE
Seat: 7A 	Price: $0.00 	AVAILABLE
Seat: 7B 	Price: $0.00 	AVAILABLE
Seat: 7C 	Price: $N/A 	NOT AVAILABLE
Seat: 7D 	Price: $14.50 	AVAILABLE
Seat: 7E 	Price: $14.50 	AVAILABLE
Seat: 7F 	Price: $14.50 	AVAILABLE
Seat: 8A 	Price: $0.00 	AVAILABLE
Seat: 8B 	Price: $0.00 	AVAILABLE
Seat: 8C 	Price: $N/A 	NOT AVAILABLE
Seat: 8D 	Price: $N/A 	NOT AVAILABLE
Seat: 8E 	Price: $0.00 	AVAILABLE
Seat: 8F 	Price: $0.00 	AVAILABLE
Seat: 9A 	Price: $N/A 	NOT AVAILABLE
Seat: 9B 	Price: $0.00 	AVAILABLE
Seat: 9C 	Price: $0.00 	AVAILABLE
Seat: 9D 	Price: $0.00 	AVAILABLE
Seat: 9E 	Price: $0.00 	AVAILABLE
Seat: 9F 	Price: $0.00 	AVAILABLE
Seat: 10A 	Price: $N/A 	NOT AVAILABLE
Seat: 10B 	Price: $0.00 	AVAILABLE
Seat: 10C 	Price: $N/A 	NOT AVAILABLE
Seat: 10D 	Price: $N/A 	NOT AVAILABLE
Seat: 10E 	Price: $0.00 	AVAILABLE
Seat: 10F 	Price: $N/A 	NOT AVAILABLE
Seat: 11A 	Price: $39.60 	AVAILABLE
Seat: 11B 	Price: $39.60 	AVAILABLE
Seat: 11C 	Price: $39.60 	AVAILABLE
Seat: 11D 	Price: $39.60 	AVAILABLE
Seat: 11E 	Price: $39.60 	AVAILABLE
Seat: 11F 	Price: $39.60 	AVAILABLE
Seat: 12A 	Price: $0.00 	AVAILABLE
Seat: 12B 	Price: $0.00 	AVAILABLE
Seat: 12C 	Price: $0.00 	AVAILABLE
Seat: 12D 	Price: $0.00 	AVAILABLE
Seat: 12E 	Price: $0.00 	AVAILABLE
Seat: 12F 	Price: $0.00 	AVAILABLE
Seat: 13A 	Price: $0.00 	AVAILABLE
Seat: 13B 	Price: $0.00 	AVAILABLE
Seat: 13C 	Price: $0.00 	AVAILABLE
Seat: 13D 	Price: $0.00 	AVAILABLE
Seat: 13E 	Price: $0.00 	AVAILABLE
Seat: 13F 	Price: $0.00 	AVAILABLE
Seat: 14A 	Price: $0.00 	AVAILABLE
Seat: 14B 	Price: $0.00 	AVAILABLE
Seat: 14C 	Price: $0.00 	AVAILABLE
Seat: 14D 	Price: $0.00 	AVAILABLE
Seat: 14E 	Price: $0.00 	AVAILABLE
Seat: 14F 	Price: $0.00 	AVAILABLE
Seat: 15A 	Price: $0.00 	AVAILABLE
Seat: 15B 	Price: $0.00 	AVAILABLE
Seat: 15C 	Price: $0.00 	AVAILABLE
Seat: 15D 	Price: $0.00 	AVAILABLE
Seat: 15E 	Price: $0.00 	AVAILABLE
Seat: 15F 	Price: $0.00 	AVAILABLE
Seat: 16A 	Price: $0.00 	AVAILABLE
Seat: 16B 	Price: $0.00 	AVAILABLE
Seat: 16C 	Price: $0.00 	AVAILABLE
Seat: 16D 	Price: $0.00 	AVAILABLE
Seat: 16E 	Price: $0.00 	AVAILABLE
Seat: 16F 	Price: $0.00 	AVAILABLE
Seat: 17A 	Price: $N/A 	NOT AVAILABLE
Seat: 17B 	Price: $N/A 	NOT AVAILABLE
Seat: 17C 	Price: $N/A 	NOT AVAILABLE
Seat: 17D 	Price: $0.00 	AVAILABLE
Seat: 17E 	Price: $0.00 	AVAILABLE
Seat: 17F 	Price: $0.00 	AVAILABLE
Seat: 18A 	Price: $N/A 	NOT AVAILABLE
Seat: 18B 	Price: $N/A 	NOT AVAILABLE
Seat: 18C 	Price: $N/A 	NOT AVAILABLE
Seat: 18D 	Price: $N/A 	NOT AVAILABLE
Seat: 18E 	Price: $0.00 	AVAILABLE
Seat: 18F 	Price: $0.00 	AVAILABLE
Seat: 19A 	Price: $N/A 	NOT AVAILABLE
Seat: 19B 	Price: $N/A 	NOT AVAILABLE
Seat: 19C 	Price: $N/A 	NOT AVAILABLE
Seat: 19D 	Price: $N/A 	NOT AVAILABLE
Seat: 19E 	Price: $0.00 	AVAILABLE
Seat: 19F 	Price: $0.00 	AVAILABLE
Seat: 20A 	Price: $0.00 	AVAILABLE
Seat: 20B 	Price: $0.00 	AVAILABLE
Seat: 20C 	Price: $0.00 	AVAILABLE
Seat: 20D 	Price: $0.00 	AVAILABLE
Seat: 20E 	Price: $0.00 	AVAILABLE
Seat: 20F 	Price: $0.00 	AVAILABLE
Seat: 21A 	Price: $0.00 	AVAILABLE
Seat: 21B 	Price: $0.00 	AVAILABLE
Seat: 21C 	Price: $0.00 	AVAILABLE
Seat: 21D 	Price: $0.00 	AVAILABLE
Seat: 21E 	Price: $0.00 	AVAILABLE
Seat: 21F 	Price: $0.00 	AVAILABLE
Seat: 22A 	Price: $0.00 	AVAILABLE
Seat: 22B 	Price: $0.00 	AVAILABLE
Seat: 22C 	Price: $0.00 	AVAILABLE
Seat: 22D 	Price: $0.00 	AVAILABLE
Seat: 22E 	Price: $0.00 	AVAILABLE
Seat: 22F 	Price: $0.00 	AVAILABLE
Seat: 23A 	Price: $0.00 	AVAILABLE
Seat: 23B 	Price: $0.00 	AVAILABLE
Seat: 23C 	Price: $0.00 	AVAILABLE
Seat: 23D 	Price: $0.00 	AVAILABLE
Seat: 23E 	Price: $0.00 	AVAILABLE
Seat: 23F 	Price: $0.00 	AVAILABLE
Seat: 24A 	Price: $0 	NOT AVAILABLE
Seat: 24B 	Price: $0 	NOT AVAILABLE
Seat: 24C 	Price: $0 	NOT AVAILABLE
Seat: 24D 	Price: $0.00 	AVAILABLE
Seat: 24E 	Price: $0.00 	AVAILABLE
Seat: 24F 	Price: $0 	NOT AVAILABLE
```
