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
    except :
        return "Error: File not found"
def change_line_c(index_1):
            FIRST_TRAIN_START = "05:00"
            TRAVEL_TIME_PER_STATION = 2 
            FIRST_TRAIN_START=FIRST_TRAIN_START.split(":")
            per_station_delay = index_1 * TRAVEL_TIME_PER_STATION 
            return per_station_delay
def index(current_station,destination_station,margenta,blueline_4,blueline_5,blueline_6,gray_line):
            station_index=0
            destination_index=1
            if current_station in margenta and destination_station in margenta :
                if margenta.index(current_station)<=margenta.index(destination_station):
                    station_index=margenta.index(current_station)
                    destination_index=margenta.index(destination_station)-station_index
                elif margenta.index(current_station)>margenta.index(destination_station) :
                    station_index=margenta[::-1].index(current_station)
                    destination_index=abs(margenta[::-1].index(destination_station)-station_index)
            if current_station in gray_line and destination_station in gray_line :
                if gray_line.index(current_station)<=gray_line.index(destination_station):
                    station_index=gray_line.index(current_station)
                    destination_index=gray_line.index(destination_station)-station_index
                elif gray_line.index(current_station)>gray_line.index(destination_station) :
                    station_index=gray_line[::-1].index(current_station)
                    destination_index=abs(gray_line[::-1].index(destination_station)-station_index)
            elif current_station in blueline_4 and destination_station in blueline_4 :
                if current_station==blueline_4[-1]and destination_station==blueline_4[0]:
                    station_index=0
                    destination_index=len(blueline_4)-1
                elif blueline_4.index(current_station)<=blueline_4.index(destination_station):
                    station_index=blueline_4.index(current_station)
                    destination_index=blueline_4.index(destination_station)-station_index
                elif blueline_4.index(current_station)>blueline_4.index(destination_station):
                    station_index=blueline_4[::-1].index(current_station)
                    destination_index=abs(blueline_4[::-1].index(destination_station)-station_index)

            elif current_station in blueline_5 and destination_station in blueline_5 :
                
               
                if blueline_5.index(current_station)<blueline_5.index(destination_station):
                    station_index=blueline_5.index(current_station)
                    destination_index=blueline_5.index(destination_station)-station_index
                elif blueline_5.index(current_station)>blueline_5.index(destination_station) :

                    station_index=blueline_5[::-1].index(current_station)
                    destination_index=abs(blueline_5[::-1].index(destination_station)-station_index)
                    

            elif ((current_station in margenta) and (destination_station not in margenta)) or ((destination_station in margenta) and (current_station not in margenta)):
                if current_station in margenta:
                    index_1=margenta.index(current_station)
                    index_2=margenta[::-1].index(current_station)
                    if change_line_c(index_1) <= change_line_c(index_2) and abs(index_1 - margenta.index("Botanical Garden")) <= abs(index_1 - margenta.index("Janakpuri West")) :
                        station_index=abs(index_1-margenta.index("Botanical Garden"))  
                    elif change_line_c(index_2) > change_line_c(index_2) and abs(index_2 - margenta.index("Botanical Garden")) <= abs(index_2 - margenta.index("Janakpuri West")):
                        station_index=abs(index_2-margenta.index("Botanical Garden"))                      
                    elif change_line_c(index_1) <= change_line_c(index_2) and abs(index_1 - margenta.index("Botanical Garden")) >= abs(index_1 - margenta.index("Janakpuri West")) :
                        station_index=abs(index_1-margenta.index("Janakpuri West"))                       
                    elif change_line_c(index_2) > change_line_c(index_2) and abs(index_2 - margenta.index("Botanical Garden")) >= abs(index_2 - margenta.index("Janakpuri West")):
                        station_index=abs(index_2-margenta.index("Janakpuri West"))
                    if destination_station in blueline_4 :
                        index_1=blueline_4.index(destination_station)
                        index_2=blueline_4[::-1].index(destination_station)
                        if change_line_c(index_1) <= change_line_c(index_2) and abs(index_1 - blueline_4.index("Botanical Garden")) <= abs(index_1 - blueline_4.index("Janakpuri West")) :
                            destination_index=abs(index_1-blueline_4.index("Botanical Garden"))+station_index-1
                        elif change_line_c(index_2) > change_line_c(index_2) and abs(index_2 - blueline_4.index("Botanical Garden")) <= abs(index_2 - blueline_4.index("Janakpuri West")):
                            destination_index=abs(index_2-blueline_4.index("Botanical Garden"))+station_index-1
                        elif change_line_c(index_1) <= change_line_c(index_2) and abs(index_1 - blueline_4.index("Botanical Garden")) >= abs(index_1 - blueline_4.index("Janakpuri West")) :
                            destination_index=abs(index_1-blueline_4.index("Janakpuri West"))+station_index-1
                        elif change_line_c(index_2) > change_line_c(index_2) and abs(index_2 - blueline_4.index("Botanical Garden")) >= abs(index_2 - blueline_4.index("Janakpuri West")):
                            destination_index=abs(index_2-blueline_4.index("Janakpuri West"))+station_index -1            
                    elif destination_station in blueline_5 and destination_station in blueline_6:
                        index_1=blueline_5.index(destination_station)
                        index_2=blueline_5[::-1].index(destination_station)
                        index_1_1=blueline_6.index(destination_station)
                        index_2_1=blueline_6[::-1].index(destination_station)
                        if abs(index_1_1 - blueline_6.index("Botanical Garden")) <= abs(index_1 - blueline_5.index("Janakpuri West")) :
                            if change_line_c(index_1_1) <= change_line_c(index_2_1):
                                destination_index=abs(index_1_1-blueline_6.index("Botanical Garden"))+station_index-1
                            else:
                                destination_index=abs(index_2_1-blueline_6.index("Botanical Garden"))+station_index-1
                        elif abs(index_1_1 - blueline_6.index("Botanical Garden")) > abs(index_1 - blueline_5.index("Janakpuri West")):
                            if change_line_c(index_1) <= change_line_c(index_2):
                                destination_index=abs(index_1-blueline_5.index("Janakpuri West"))+station_index-1                        
                            else:
                                destination_index=abs(index_2-blueline_5.index("Janakpuri West"))+station_index-1
                elif destination_station in margenta:
                    index_1=margenta.index(destination_station)
                    index_2=margenta[::-1].index(destination_station)
                    if change_line_c(index_1) <= change_line_c(index_2) and abs(index_1 - margenta.index("Botanical Garden")) <= abs(index_1 - margenta.index("Janakpuri West")) :
                        station_index=abs(index_1-margenta.index("Botanical Garden"))  
                    elif change_line_c(index_2) > change_line_c(index_2) and abs(index_2 - margenta.index("Botanical Garden")) <= abs(index_2 - margenta.index("Janakpuri West")):
                        station_index=abs(index_2-margenta.index("Botanical Garden"))                      
                    elif change_line_c(index_1) <= change_line_c(index_2) and abs(index_1 - margenta.index("Botanical Garden")) >= abs(index_1 - margenta.index("Janakpuri West")) :
                        station_index=abs(index_1-margenta.index("Janakpuri West"))                       
                    elif change_line_c(index_2) > change_line_c(index_2) and abs(index_2 - margenta.index("Botanical Garden")) >= abs(index_2 - margenta.index("Janakpuri West")):
                        station_index=abs(index_2-margenta.index("Janakpuri West"))
                    if current_station in blueline_4 :
                        index_1=blueline_4.index(current_station)
                        index_2=blueline_4[::-1].index(current_station)
                        if change_line_c(index_1) <= change_line_c(index_2) and abs(index_1 - blueline_4.index("Botanical Garden")) <= abs(index_1 - blueline_4.index("Janakpuri West")) :
                            destination_index=abs(index_1-blueline_4.index("Botanical Garden"))+station_index-1
                        elif change_line_c(index_2) > change_line_c(index_2) and abs(index_2 - blueline_4.index("Botanical Garden")) <= abs(index_2 - blueline_4.index("Janakpuri West")):
                            destination_index=abs(index_2-blueline_4.index("Botanical Garden"))+station_index-1
                        elif change_line_c(index_1) <= change_line_c(index_2) and abs(index_1 - blueline_4.index("Botanical Garden")) >= abs(index_1 - blueline_4.index("Janakpuri West")) :
                            destination_index=abs(index_1-blueline_4.index("Janakpuri West"))+station_index-1
                        elif change_line_c(index_2) > change_line_c(index_2) and abs(index_2 - blueline_4.index("Botanical Garden")) >= abs(index_2 - blueline_4.index("Janakpuri West")):
                            destination_index=abs(index_2-blueline_4.index("Janakpuri West"))+station_index -1
                    elif current_station in blueline_5 and current_station in blueline_6:
                        index_1=blueline_5.index(current_station)
                        index_2=blueline_5[::-1].index(current_station)
                        index_1_1=blueline_6.index(current_station)
                        index_2_1=blueline_6[::-1].index(current_station)
                        if abs(index_1_1 - blueline_6.index("Botanical Garden")) <= abs(index_1 - blueline_5.index("Janakpuri West")) :
                            if change_line_c(index_1_1) <= change_line_c(index_2_1):
                                destination_index=abs(index_1_1-blueline_6.index("Botanical Garden"))+station_index-1
                            else:
                                destination_index=abs(index_2_1-blueline_6.index("Botanical Garden"))+station_index-1
                        elif abs(index_1_1 - blueline_6.index("Botanical Garden")) > abs(index_1 - blueline_5.index("Janakpuri West")):
                            if change_line_c(index_1) <= change_line_c(index_2):
                                destination_index=abs(index_1-blueline_5.index("Janakpuri West"))+station_index-1
                            else:
                                destination_index=abs(index_2-blueline_5.index("Janakpuri West"))+station_index-1
            return station_index,destination_index
def calculate_next_train(current_station, stations, current_time, margenta,blueline_4,blueline_5,blueline_6,destination_station,gray_line):
        try:
            FIRST_TRAIN_START = "06:00"
            LAST_TRAIN_TIME="23:00"
            TRAVEL_TIME_PER_STATION = 2              
            station_index,destination_index=index(current_station,destination_station,margenta,blueline_4,blueline_5,blueline_6,gray_line)
            a=current_time
            current_time=current_time.split(":")
            current_minutes = int(current_time[0]) * 60 + int(current_time[1])
            if (current_minutes >8*60 and current_minutes < 10*60) or (current_minutes >17*60 and current_minutes < 19*60):
                TRAIN_INTERVAL = 4
            else:
                TRAIN_INTERVAL = 8        
            FIRST_TRAIN_START=FIRST_TRAIN_START.split(":")
            FIRST_TRAIN_START = int(FIRST_TRAIN_START[0]) * 60 + int(FIRST_TRAIN_START[1])
            per_station_delay = station_index * TRAVEL_TIME_PER_STATION 
            first_train_arrival_to_station = FIRST_TRAIN_START + per_station_delay
            train_number = 0
            while True:
                train_arrival_time = first_train_arrival_to_station + (train_number * TRAIN_INTERVAL)
                train_final_time = (destination_index*TRAVEL_TIME_PER_STATION)+train_arrival_time
                if train_arrival_time >= current_minutes:
                    arrival_hour = int(train_arrival_time) // 60
                    arrival_minute = train_arrival_time-(arrival_hour*60)
                    final_hour = int(train_final_time) // 60
                    final_minute = train_final_time-(final_hour*60)
                    wait_time = train_arrival_time - current_minutes               
                    return {   
                        "current station": current_station,
                        "destination station": destination_station,
                        "arrival time": f"{arrival_hour}:{arrival_minute}",
                        "wait minutes": wait_time,
                        "current time": a,
                        "Journey min": train_final_time-train_arrival_time,
                        "Journey duration": f"{final_hour}:{final_minute}"
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
blueline_1=stations_only[40:48]#vaishali line
blueline_2=stations_only[24:40]#ele to akshardham
blueline_3=stations_only[65:98]#inderpreastha to dwarka
blueline_4=stations_only[48:98]#main blueline from ele
blueline_5=blueline_1+blueline_3#main blueline from vaishali
blueline_6=blueline_1+blueline_2[::-1]
gray_line=stations_only[99:]
print(gray_line)
for i, station in enumerate(stations_only, 1):
    if station in margenta and station in blueline_4 :
        print(f"{i}.    station on both blue and margenta lines: {station}")
    elif station in margenta and station in blueline_5 :
        print(f"{i}.    station on both blue and margenta lines: {station}")
    elif station in margenta:
        print(f"{i}.    margenta line station: {station}")
    elif station in gray_line:
        print(f"{i}.    gray line station: {station}")
    elif station in blueline_4 or blueline_5:
        print(f"{i}.    blue line station: {station}")
        
print(  "=" * 50)
current_station = input("Enter your current station name: ").strip()
destination_station=input("Enter your destination station name: ").strip()
current_time=input("Enter current time (kindly enter in 24 hrs format) :").strip()
result = calculate_next_train(current_station, cmplt_info,current_time,margenta,blueline_4,blueline_5,blueline_6,destination_station,gray_line)
print( "=" * 50)
print("TRAVEL DETAILS")
print("=" * 50)
current_time=current_time.split(":")
current_minutes = int(current_time[0]) * 60 + int(current_time[1])
if current_minutes > 23*60:
                print(" Metro Closed")
else:
    print("Current Station line: ",cmplt_info[stations_only.index(current_station)][0])
    print("Current Station: ",result['current station'])
    print("Destination Station line:",cmplt_info[stations_only.index(destination_station)][0])
    print("Destination Station: ",result['destination station'])
    if cmplt_info[stations_only.index(destination_station)][0] != cmplt_info[stations_only.index(current_station)][0] :
        print("Interchange required")
    else:
        print("No Interchange required")
    print("Current Time: ",result['current time'])
    print("Train Arrival Time: ",result['arrival time'])
    print("Waiting Time: ",result['wait minutes'])
    print("journey Time in minutes :",result['Journey min'])
    print("journey Time: ",result['Journey duration'])
print("=" * 50)