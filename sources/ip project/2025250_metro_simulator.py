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
def index(current_station,destination_station,margenta,blueline_4,blueline_5,blueline_6,gray_line,Yellow):
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
            if current_station in Yellow and destination_station in Yellow :
                if Yellow.index(current_station)<=Yellow.index(destination_station):
                    station_index=Yellow.index(current_station)
                    destination_index=Yellow.index(destination_station)-station_index
                elif Yellow.index(current_station)>Yellow.index(destination_station) :
                    station_index=Yellow[::-1].index(current_station)
                    destination_index=abs(Yellow[::-1].index(destination_station)-station_index)
            elif current_station in blueline_4 and destination_station in blueline_4 :
                if blueline_4.index(current_station)<=blueline_4.index(destination_station):
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
                    if destination_station in blueline_4 :
                        index_1=blueline_4.index(destination_station)
                        index_2=blueline_4[::-1].index(destination_station)
                        if abs(index_1 - blueline_4.index("Botanical Garden")) <= abs(index_1 - blueline_4.index("Janakpuri West")) :
                            station_index=abs(margenta.index(current_station)-margenta.index("Botanical Garden"))
                            destination_index=abs(index_1-blueline_4.index("Botanical Garden"))+station_index-1
                            station_index=margenta.index(current_station)
                        else:
                            station_index=abs(margenta.index(current_station)-margenta.index("Janakpuri West"))
                            destination_index=abs(index_2-blueline_4.index("Janakpuri West"))+station_index-1
                            station_index=margenta[::-1].index(current_station)          
                    elif destination_station in blueline_5 and destination_station in blueline_6:
                        index_1=blueline_5.index(destination_station)
                        index_2=blueline_5[::-1].index(destination_station)
                        index_1_1=blueline_6.index(destination_station)
                        index_2_1=blueline_6[::-1].index(destination_station)
                        if abs(index_1_1 - blueline_6.index("Botanical Garden")) <= abs(index_1 - blueline_5.index("Janakpuri West")) or abs(index_2_1 - blueline_6[::-1].index("Botanical Garden")) <= abs(index_2 - blueline_5[::-1].index("Janakpuri West")):
                            station_index=(margenta.index(current_station)-margenta.index("Botanical Garden"))
                            if change_line_c(index_1_1) <= change_line_c(index_2_1):
                                destination_index=abs(index_1_1-blueline_6.index("Botanical Garden"))+station_index-1
                                station_index=margenta.index(current_station)
                            else:
                                destination_index=abs(index_2_1-blueline_6[::-1].index("Botanical Garden"))+station_index-1
                                station_index=margenta[::-1].index(current_station)
                        else:
                            station_index=abs(margenta.index(current_station)-margenta.index("Botanical Garden"))
                            if change_line_c(index_1) <= change_line_c(index_2):
                                destination_index=abs(index_1-blueline_5.index("Janakpuri West"))+station_index-1   
                                station_index=blueline_5.index(current_station)                     
                            else:
                                destination_index=abs(index_2-blueline_5[::-1].index("Janakpuri West"))+station_index-1
                                station_index=blueline_5[::-1].index(current_station)
                elif destination_station in margenta:
                    a,b=current_station,destination_station
                    current_station,destination_station=destination_station,current_station
                    if destination_station in blueline_4 :
                        index_1=blueline_4.index(destination_station)
                        index_2=blueline_4[::-1].index(destination_station)
                        if abs(index_1 - blueline_4.index("Botanical Garden")) <= abs(index_1 - blueline_4.index("Janakpuri West")) :
                            station_index=abs(margenta.index(current_station)-margenta.index("Botanical Garden"))
                            destination_index=abs(index_1-blueline_4.index("Botanical Garden"))+station_index-1
                            station_index=margenta.index(current_station)
                        else:
                            station_index=abs(margenta.index(current_station)-margenta.index("Janakpuri West"))
                            destination_index=abs(index_2-blueline_4.index("Janakpuri West"))+station_index-1
                            station_index=margenta[::-1].index(current_station)          
                    elif destination_station in blueline_5 and destination_station in blueline_6:
                        index_1=blueline_5.index(destination_station)
                        index_2=blueline_5[::-1].index(destination_station)
                        index_1_1=blueline_6.index(destination_station)
                        index_2_1=blueline_6[::-1].index(destination_station)
                        if abs(index_1_1 - blueline_6.index("Botanical Garden")) <= abs(index_1 - blueline_5.index("Janakpuri West")) or abs(index_2_1 - blueline_6[::-1].index("Botanical Garden")) <= abs(index_2 - blueline_5[::-1].index("Janakpuri West")):
                            station_index=(margenta.index(current_station)-margenta.index("Botanical Garden"))
                            if change_line_c(index_1_1) <= change_line_c(index_2_1):
                                destination_index=abs(index_1_1-blueline_6.index("Botanical Garden"))+station_index-1
                                station_index=margenta.index(current_station)
                            else:
                                destination_index=abs(index_2_1-blueline_6[::-1].index("Botanical Garden"))+station_index-1
                                station_index=margenta[::-1].index(current_station)
                        else:
                            station_index=abs(margenta.index(current_station)-margenta.index("Botanical Garden"))
                            if change_line_c(index_1) <= change_line_c(index_2):
                                destination_index=abs(index_1-blueline_5.index("Janakpuri West"))+station_index-1   
                                station_index=blueline_5.index(current_station)                     
                            else:
                                destination_index=abs(index_2-blueline_5[::-1].index("Janakpuri West"))+station_index-1
                                station_index=blueline_5[::-1].index(current_station)
                    
                      
                    index_1=margenta.index(b)
                    index_2=margenta[::-1].index(b)
                    if change_line_c(index_1) < change_line_c(index_2) :
                        station_index=abs(index_1-margenta.index("Botanical Garden"))  
                    else:
                        station_index=abs(index_2-margenta[::-1].index("Janakpuri West"))                     
            return station_index,destination_index
def calculate_next_train(current_station, stations, current_time, margenta,blueline_4,blueline_5,blueline_6,destination_station,gray_line,Yellow):
        #try:
            FIRST_TRAIN_START = "06:00"
            LAST_TRAIN_TIME="23:00"
            TRAVEL_TIME_PER_STATION = 2 # + 0.33 -->  this is the train wait time at each station (20/60)
            station_index,destination_index=index(current_station,destination_station,margenta,blueline_4,blueline_5,blueline_6,gray_line,Yellow)
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
                        "next train time": f"{arrival_hour}:{arrival_minute+(1*TRAIN_INTERVAL)}, {arrival_hour}:{arrival_minute+(2*TRAIN_INTERVAL)}, {arrival_hour}:{arrival_minute+(3*TRAIN_INTERVAL)}",
                        "wait minutes": wait_time,
                        "current time": a,
                        "Journey min": train_final_time-train_arrival_time,
                        "Journey duration": f"{final_hour}:{final_minute}"
                        }              
                train_number += 1
        #except:
             #return "error"
def main(): 
    print("=" * 50)
    print("TRAIN ARRIVAL CALCULATOR")
    print("=" * 50)
    filename = input("Enter the station list filename:").strip()
    stations_only,cmplt_info = load_stations(filename)
    margenta=stations_only[:25]#margenta
    blueline_1=stations_only[41:49]#vaishali line
    blueline_2=stations_only[24:41]#ele to akshardham
    blueline_3=stations_only[65:99]#inderpreastha to dwarka
    blueline_4=stations_only[48:98]#main blueline from ele
    blueline_5=blueline_1+blueline_3#main blueline from vaishali
    blueline_6=blueline_1+blueline_2[::-1]
    Yellow=stations_only[104:]
    gray_line=stations_only[99:104]
    for i, station in enumerate(stations_only, 1):
        if station in margenta and station in blueline_4 :
            print(f"{i}.    station on both blue and margenta lines: {station}")
        elif station in margenta and station in blueline_5 :
            print(f"{i}.    station on both blue and margenta lines: {station}")
        elif station in gray_line and station in blueline_4:
            print(f"{i}.    station on both blue and gray line station: {station}")
        elif station in gray_line and station in blueline_5:
            print(f"{i}.    station on both yellow and gray line station: {station}")
        elif station in Yellow and station in blueline_5:
            print(f"{i}.    station on both blue and yellow line station: {station}")
        elif station in Yellow and station in blueline_4:
            print(f"{i}.    station on both blue and yellow line station: {station}")
        elif station in Yellow and station in margenta:
            print(f"{i}.    station on both blue and margenta line station: {station}")
        elif station in Yellow: 
            print(f"{i}.    Yellow line station: {station}")
        elif station in gray_line:
            print(f"{i}.    gray line station: {station}")
        elif station in margenta:
            print(f"{i}.    margenta line station: {station}")
        elif station in blueline_4 or blueline_5:
            print(f"{i}.    blue line station: {station}")
        
        
        
    print(  "=" * 50)
    current_station = input("Enter your current station name: ").strip()
    destination_station=input("Enter your destination station name: ").strip()
    current_time=input("Enter current time (kindly enter in 24 hrs format) :").strip()
    result = calculate_next_train(current_station, cmplt_info,current_time,margenta,blueline_4,blueline_5,blueline_6,destination_station,gray_line,Yellow)
    print( "=" * 50)
    print("TRAVEL DETAILS")
    print("=" * 50)
    current_time=current_time.split(":")
    current_minutes = int(current_time[0]) * 60 + int(current_time[1])
    if current_minutes > 23*60:
                    print("No service available")
    else:
        print("Current Station line: ",cmplt_info[stations_only.index(current_station)][0])
        print("Current Station: ",result['current station'])
        print("Destination Station line:",cmplt_info[stations_only.index(destination_station)][0])
        print("Destination Station: ",result['destination station'])
        print("Current Time: ",result['current time'])
        print("Train Arrival Time: ",result['arrival time'])
        print("Consecutive Train Arrival Time: ",result['next train time'])
        ride_planner=input("do you want further comprehensive journey planner ? yes / no ").strip().upper()
        if ride_planner=="YES":
            print( "=" * 50)
            print("JourneyPlanner")
            print("=" * 50)
            if cmplt_info[stations_only.index(destination_station)][0] != cmplt_info[stations_only.index(current_station)][0] :
                print("Interchange required")
            else:
                print("No Interchange required")
            print("Rider can catch train from the starting station at: ",result['current station'])
            print("Waiting Time: ",result['wait minutes'])
            print("journey Time in minutes :",result['Journey min'])
            print("journey Time: ",result['Journey duration'])
        
    print("=" * 50)
main()
