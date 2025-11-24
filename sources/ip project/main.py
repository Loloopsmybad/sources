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
            destination_station_index=0
            
            
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
def calculate_next_train(current_station, stations, current_time):
        try:
            
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
           
                if train_arrival_time >= current_minutes:

                    arrival_hour = int(train_arrival_time) // 60
                    arrival_minute = train_arrival_time-(arrival_hour*60)
           
                

                    wait_time = train_arrival_time - current_minutes
                   
                    
                    
                    return {   
                        
                        }
                
                train_number += 1
        except:
            return "error"

print("=" * 50)
print("TRAIN ARRIVAL CALCULATOR")
print("=" * 50)

filename = input("Enter the station list filename:").strip()

stations,cmplt_info = load_stations(filename)

margenta=stations[:25]
m_e=25
blueline_1=stations[42:50]
b1_s=42
b1_e=50
blueline_2=stations[26:42]
blueline_3=stations[50:100]
b3_s=50
b3_e=100

for i, station in enumerate(stations, 1):
    if station in margenta and station in blueline_1 :
        print(f"{i}.    station on both blue and martgenta lines: {station}")
    elif station in margenta and station in blueline_3 :
        print(f"{i}.    station on both blue and martgenta lines: {station}")
    elif station in margenta:
        print(f"{i}.    margenta line station: {station}")
    elif station in blueline_1 or blueline_3:
        print(f"{i}.    blue line station: {station}")
     
print("\n" + "=" * 50)
current_line=input("Enter your current station line: ").strip().upper()
current_station = input("Enter your current station name: ").strip()
destination_line=input("Enter your destination station line: ").strip()
destination_station=input("Enter your destination station name: ").strip().upper()
interchange_station=input("Enter the station name at which you want to change line ('NA' if not change):")
current_time=input("Enter current time (kindly enter in 24 hrs format) :").strip()
if interchange_station=="NA":
    interchange_station=current_line


result = calculate_next_train(current_station, cmplt_info,current_time)

print("\n" + "=" * 50)
print("TRAVEL DETAILS")
print("=" * 50)

if "error" in result:
    print("Error")
else:
    print(f"Current Station line: {current_line}")
    print(f"Current Station: {result['station']}")
    print(f"Destination Station line: {destination_line}")
    print(f"Destination Station: {result['station']}")
    print(f"Current Time: {result['current time']}")
    print(f"Train Arrival Time: {result['arrival time']}")
    print(f"Waiting Time: {result['wait minutes']} minutes")

print("=" * 50)

