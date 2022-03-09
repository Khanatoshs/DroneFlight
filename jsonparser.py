import sys
import json

if __name__ == '__main__':

    #Read console arguments
    lArg = sys.argv

    #Json file where the coordinates are from
    tableFile = lArg[1]
    #Json file where the flight path will be made
    resultFile = lArg[2]

    #Open json file with coordinates
    with open(tableFile) as jsonTable:
        #Create structure of flightpath json
        flightJson = {
        "heading_mode": "TOWARD_POINT_OF_INTEREST",
        "fineshed_action": "GO_HOME",
        "flight_path_mode": "NORMAL",
        "goto_waypoint_mode": "SAFELY",
        "max_flight_speed": 10,
        "auto_flight_speed": 5,
        "repeat_times": 1,
        "point_of_interest": [41.84182360, 140.76696396],
        "exit_mission_on_rc_signal_lost_enabled": False,
        "gimbal_pitch_rotation_enabled": True,
        "waypoint_list":[]
        }
        #Read json data from table into dictionary
        data = json.load(jsonTable)
        #Go trhough all coordinates in the table
        for dat in data['features']:
            #Create waypoint of the structure
            waypoint = {   
                "order": 0,
                "coordinate": [],
                "altitude": 70,
                "corner_radius": 0.2,
                "turn_mode": "CLOCKWISE",
                "gimbal_pitch": -90,
                "speed": 3,
                "action_list":[]
            }
            #Add coordinates to waypoint
            waypoint['coordinate'].append(dat['properties']['y'])
            waypoint['coordinate'].append(dat['properties']['x'])
            flightJson['waypoint_list'].append(waypoint)
        #Create resultjson file where flightpath is
        with open(resultFile,'w') as outfile:
            json.dump(flightJson,outfile)


