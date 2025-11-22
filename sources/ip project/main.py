from datetime import datetime, timedelta

def load_stations(filename):
    try:
        with open(filename, 'r') as f:
            stations = f.readlines()
            for i in range(len(stations)) :
                stations[i] = stations[i].strip()
            for i in range(len(stations)):
                stations[i] = stations[i].split(",")
        return stations
    except FileNotFoundError:
        return f"Error: File '{filename}' not found."

def calculate_next_train(current_station, stations, current_time):
    FIRST_TRAIN_START = "05:00"
    TRAVEL_TIME_PER_STATION = 5  
    TRAIN_INTERVAL = 8 
    station_index=0
    for i in range(len(stations)):
        if i=="current_station":
            break
        station_index+=1

    travel_time_to_station = station_index * TRAVEL_TIME_PER_STATION 
    current_time=current_time.split(":")
    current_minutes = int(current_time[0]) * 60 + int(current_time[1])
    FIRST_TRAIN_START=FIRST_TRAIN_START.split()
    FIRST_TRAIN_START = int(FIRST_TRAIN_START[0]) * 60 + int(current_time[1])
    first_train_arrival_to_station = FIRST_TRAIN_START + travel_time_to_station
    train_number = 0
    while True:
        train_arrival_time = first_train_arrival_to_station + (train_number * TRAIN_INTERVAL)
        
        if train_arrival_time >= current_minutes:
            # Found the next train
            arrival_hour = int(train_arrival_time // 60)
            arrival_minute = int(train_arrival_time % 60)
            
            # Create arrival datetime
            arrival_datetime = current_time.replace(hour=arrival_hour, minute=arrival_minute, second=0, microsecond=0)
            
            # If calculated time is before current time, it means it's tomorrow
            if arrival_datetime < current_time:
                arrival_datetime += timedelta(days=1)
            
            # Calculate waiting time
            wait_time = arrival_datetime - current_time
            wait_minutes = int(wait_time.total_seconds() / 60)
            
            return {
                "station": current_station,
                "station_number": station_index + 1,
                "total_stations": len(stations),
                "train_number": train_number + 1,
                "arrival_time": arrival_datetime.strftime("%I:%M %p"),
                "wait_minutes": wait_minutes,
                "current_time": current_time.strftime("%I:%M %p")
            }
        
        train_number += 1
        



print("=" * 50)
print("TRAIN ARRIVAL CALCULATOR")
print("=" * 50)

filename = input("Enter the station list filename:").strip()

stations = load_stations(filename)

for i, station in enumerate(stations, 1):
    print(f"{i}. {station[1]}")


print("\n" + "=" * 50)

current_station = input("Enter your current station name: ").strip()
current_time=input("Enter current time:").strip()

result = calculate_next_train(current_station, stations,current_time)

print("\n" + "=" * 50)
print("RESULT")
print("=" * 50)

if "error" in result:
    print(f"Error: {result['error']}")
else:
    print(f"Current Station: {result['station']}")
    print(f"Station Position: {result['station_number']} of {result['total_stations']}")
    print(f"Current Time: {result['current_time']}")
    print(f"Next Train (Train #{result['train_number']}): {result['arrival_time']}")
    print(f"Waiting Time: {result['wait_minutes']} minutes")

print("=" * 50)

print(load_stations("metro_stations_csv.txt"))