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
        try:
            FIRST_TRAIN_START = "05:00"
            TRAVEL_TIME_PER_STATION = 2  
            TRAIN_INTERVAL = 8 
            station_index=0
            for i in range(len(stations)):
                if stations[i][1] ==current_station:
                    
                    break
                station_index+=1
            
            #print(station_index)
            

            a=current_time
            current_time=current_time.split(":")
            current_minutes = int(current_time[0]) * 60 + int(current_time[1])
            #print(f"{current_minutes}min")
            FIRST_TRAIN_START=FIRST_TRAIN_START.split(":")
            FIRST_TRAIN_START = int(FIRST_TRAIN_START[0]) * 60 + int(FIRST_TRAIN_START[1])

            per_station_delay = station_index * TRAVEL_TIME_PER_STATION 
            # print("hi1",per_station_delay)
            first_train_arrival_to_station = FIRST_TRAIN_START + per_station_delay
            # print("hi",first_train_arrival_to_station)
            train_number = 0
            while True:
                train_arrival_time = first_train_arrival_to_station + (train_number * TRAIN_INTERVAL)
                #print(train_arrival_time)
                if train_arrival_time >= current_minutes:

                    arrival_hour = int(train_arrival_time) // 60
                    arrival_minute = train_arrival_time-(arrival_hour*60)
                    #print("minutes",arrival_minute)
                

                    wait_time = train_arrival_time - current_minutes
                    #wait_hour = int(wait_time // 60)
                    #wait_minute = int(wait_time % 60)
                    #print(f"{wait_minute}")
                    
                    
                    return {   
                        "station": current_station,
                        "arrival time": f"{arrival_hour}:{arrival_minute}",
                        "wait minutes": wait_time,
                        "current time": a
                        }
                
                train_number += 1
        except:
            return "error"








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
print("TRAVEL DETAILS")
print("=" * 50)

if "error" in result:
    print("Error")
else:
    print(f"Current Station: {result['station']}")
    print(f"Current Time: {result['current time']}")
    print(f"Train Arrival Time: {result['arrival time']}")
    print(f"Waiting Time: {result['wait minutes']} minutes")

print("=" * 50)

