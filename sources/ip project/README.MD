
how to run:
==================================================
Install Python 3 or above
keep the python file and the station liist file in the same diirectory
use 24 hrs clock while entering the current time
the data file metro_data.txt should be in the same folder as the python file metro.py


Features:
==================================================
Identifies stations in the following line:
        Magenta Line
        Blue Line (multiple stretches: BL4, BL5, BL6)
        Gray Line
Determines:
    Current station index
    Destination station index
    Line-based routing (including interchanges)
    Travel time between stations
Calculates:
    Next train arrival time
    Waiting time
    Total journey time
    Whether interchange is required

Load Stations
==================================================
The load_stations() function reads the file and extracts:
station_names: a list of station names
complete_info: full rows split as [line, station]

Line Definitions
==================================================
The list slicing the station list into separate line lists:
margenta
blueline_4
blueline_5
blueline_6
gray_line

Station Index Calculation
==================================================
The index() function:
Identifies the distance/number of stations between current & destination station
Handles reverse-direction travel
Handles interchange logic between lines

Time Calculation
==================================================
The program considers:
First train at 6:00
Peak hours:
08:00–10:00
17:00–19:00
Peak interval: 4 minutes
Off-peak interval: 8 minutes
Travel time per station: 2 minutes
First train at 23:00 or 11:00 pm


Assumptions:
==================================================
Travel time between all stations = 2 minutes
there are no interchanges to gray line
Station order in the file is correct
No realtime delays are considered




example output:
==================================================

TRAVEL DETAILS
==================================================
Current Station line: Magenta
Current Station: Okhla NSIC
Destination Station line: Blue Line
Destination Station: Rajiv Chowk
Interchange required
Current Time: 18:20
Train Arrival Time: 18:24
Waiting Time: 4 minutes
Journey Time in minutes: 22
Journey Time: 18:46



STATION LIIST DATA FORMAT
==================================================
EXAMPLE DATA
    STATIONLINE,CURRENT STATION,NEXT STATION GOING FROM TOP TO BOTTOM,INTERCHANGE,DISTANCE BETWEEN STATIONS
    MARGENTA,Botanical Garden,Okhla Bird Sanctuary,YES,2
    MARGENTA,Okhla Bird Sanctuary,Kalindi Kunj,NO,2
    MARGENTA,Kalindi Kunj,Jasola Vihar Shaheen Bagh,NO,2
    MARGENTA,Jasola Vihar Shaheen Bagh,Okhla Vihar,NO,2
    MARGENTA,Okhla Vihar,Jamia Millia Islamia,NO,2
    MARGENTA,Jamia Millia Islamia,Sukhdev Vihar,NO,2
