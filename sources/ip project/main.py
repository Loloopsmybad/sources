def load_stations(filename):
    try:
        with open(filename,'r') as f:
            stations = f.readlines()
            station_names=[]
            for i in range(len(stations)) :
                stations[i] = stations[i].strip()
            for i in range(len(stations)):
                stations[i] = stations[i].split(",")
            for i in range(len(stations)):
                station_names.append(stations[i][1])
        return station_names,stations
    except FileNotFoundError:
        return f"Error: File '{filename}' not found."

def calculate_next_train(current_station, stations, current_time, margenta,blueline_4,blueline_5):
        try:
            FIRST_TRAIN_START = "05:00"
            TRAVEL_TIME_PER_STATION = 2  
            TRAIN_INTERVAL = 8 
            station_index=0
            destination_index=0
            # if current_station in margenta:
            #     station_index=margenta.index(current_station)
            # elif current_station in blueline_1:
            #     station_index=blueline_1.index(current_station)
            # elif current_station in blueline_3:
            #     station_index=blueline_3.index(current_station)

            # for i in range(len(stations)):
            #             if stations[i][1] ==current_station:   
            #                 break
            #             station_index+=1
            print(destination_station in margenta)
            if current_station in margenta and destination_station in margenta :
                print("hi")
                if margenta.index(current_station)<margenta.index(destination_station):
                    station_index=margenta.index(current_station)
                    destination_index=margenta.index(destination_index)-station_index
                elif margenta.index(current_station)>margenta.index(destination_station):
                    margenta=margenta[::-1]
                    station_index=margenta.index(current_station)
                    destination_index=abs(margenta.index(destination_station)-station_index)
            elif current_station in blueline_4 and destination_station in blueline_4 :
                print("hi")
                if blueline_4.index(current_station)<blueline_4.index(destination_station):
                    station_index=blueline_4.index(current_station)
                    destination_index=blueline_4.index(destination_station)-station_index
                elif blueline_4.index(current_station)>blueline_4.index(destination_station):
                    blueline_4=blueline_4[::-1]
                    station_index=blueline_4.index(current_station)
                    destination_index=abs(blueline_4.index(destination_station)-station_index)
            elif current_station in blueline_5 and destination_station in blueline_5 :
                print("hi")
                if blueline_5.index(current_station)<blueline_5.index(destination_station):
                    station_index=blueline_5.index(current_station)
                    destination_index=blueline_5.index(destination_station)-station_index
                elif blueline_5.index(current_station)>blueline_5.index(destination_station):
                    blueline_5=blueline_5[::-1]
                    station_index=blueline_5.index(current_station)
                    destination_index=abs(blueline_5.index(destination_station)-station_index)

            # elif current_station in margenta and destination_station in blueline_3:
            #         station_index=margenta.index(current_station)
            #         if station.index()
            #         destination_index=blueline_3.index(destination_index)
            print(station_index)
            print(destination_index)
            

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
                    wait_time = train_arrival_time - current_minutes
                    
                    return {   
                        "current station": current_station,
                        "destination station": destination_station,
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

stations_only,cmplt_info = load_stations(filename)

margenta=stations_only[:25]#margenta
blueline_1=stations_only[42:50]#vaishali line
blueline_2=stations_only[26:42]#ele to akshardham
blueline_3=stations_only[67:100]#inderpreastha to dwarka
blueline_4=stations_only[50:100]#main blueline from ele
blueline_5=blueline_1+blueline_3#main blueline from vaishali


for i, station in enumerate(stations_only, 1):
    if station in margenta and station in blueline_1 :
        print(f"{i}.    station on both blue and margenta lines: {station}")
    elif station in margenta and station in blueline_4 :
        print(f"{i}.    station on both blue and margenta lines: {station}")
    elif station in margenta:
        print(f"{i}.    margenta line station: {station}")
    elif station in blueline_1 or blueline_4:
        print(f"{i}.    blue line station: {station}")
     
print("\n" + "=" * 50)

current_station = input("Enter your current station name: ").strip()
destination_station=input("Enter your destination station name: ").strip()
current_time=input("Enter current time (kindly enter in 24 hrs format) :").strip()

result = calculate_next_train(current_station, cmplt_info,current_time,margenta,blueline_4,blueline_5)

print("\n" + "=" * 50)
print("TRAVEL DETAILS")
print("=" * 50)

if "error" in result:
    print("Error")
else:
    print(f"Current Station line: {cmplt_info[stations_only.index(current_station)][0]}")
    print(f"Current Station: {result['current station']}")
    print(f"Destination Station line: {cmplt_info[stations_only.index(destination_station)][0]}")
    print(f"Destination Station: {result['destination station']}")
    print(f"Current Time: {result['current time']}")
    print(f"Train Arrival Time: {result['arrival time']}")
    print(f"Waiting Time: {result['wait minutes']} minutes")

print("=" * 50)

