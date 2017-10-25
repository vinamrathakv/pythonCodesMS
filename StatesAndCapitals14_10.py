
statesCapitals   = {
                    "Alabama":"Montgomery",
                    "Alaska":"Juneau",
                    "Arizona":"Phoenix",
                    "Arkansas":"Little Rock",
                    "California":"Sacramento",
                    "Colorado":"Denver",
                    "Connecticut":"Hartford",
                    "Delaware":"Dover",
                    "Florida":"Tallahassee",
                    "Georgia":"Atlanta",
                    "Hawaii":"Honolulu",
                    "Idaho":"Boise",
                    "Illinois":"Springfield",
                    "Indiana":"Indianapolis",
                    "Iowa":"Des Moines",
                    "Kansas":"Topeka",
                    "Kentucky":"Frankfort",
                    "Louisiana":"Baton Rouge",
                    "Maine":"Augusta",
                    "Maryland":"Annapolis",
                    "Massachusettes":"Boston",
                    "Michigan":"Lansing",
                    "Minnesota":"Saint Paul",
                    "Mississippi":"Jackson",
                    "Missouri":"Jefferson City",
                    "Montana":"Helena",
                    "Nebraska":"Lincoln",
                    "Nevada":"Carson City",
                    "New Hampshire":"Concord",
                    "New Jersey":"Trenton",
                    "New York":"Albany",
                    "New Mexico":"Santa Fe",
                    "North Carolina":"Raleigh",
                    "North Dakota":"Bismark",
                    "Ohio":"Columbus",
                    "Oklahoma":"Oklahoma City",
                    "Oregon":"Salem",
                    "Pennslyvania":"Harrisburg",
                    "Rhode Island":"Providence",
                    "South Carolina":"Columbia",
                    "South Dakota":"Pierre",
                    "Tennessee":"Nashville",
                    "Texas":"Austin",
                    "Utah":"Salt Lake City",
                    "Vermont":"Montpelier",
                    "Virginia":"Richmond",
                    "Washington":"Olympia",
                    "West Virginia":"Charleston",
                    "Wisconsin":"Madison",
                    "Wyoming":"Cheyenne"}
states = statesCapitals.keys()

print("Enter the capital of the displayed state :")
count = 0

for state in states:
    capital = input(state + "= ")
    if capital.lower() == statesCapitals[state].lower():
        count += 1
    else:
        print("Correct capital is : ",statesCapitals[state] )
    
        
print(count)        
        
        